// Licensed to the Apache Software Foundation (ASF) under one
// or more contributor license agreements.  See the NOTICE file
// distributed with this work for additional information
// regarding copyright ownership.  The ASF licenses this file
// to you under the Apache License, Version 2.0 (the
// "License"); you may not use this file except in compliance
// with the License.  You may obtain a copy of the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing,
// software distributed under the License is distributed on an
// "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
// KIND, either express or implied.  See the License for the
// specific language governing permissions and limitations
// under the License.

use std::io::SeekFrom;
use std::task::ready;
use std::task::Context;
use std::task::Poll;

use bytes::Bytes;
use tokio::io::ReadBuf;

use crate::raw::*;
use crate::*;

/// into_streamable is used to make [`oio::Read`] or [`oio::BlockingRead`] streamable.
pub fn into_streamable_read<R>(r: R, capacity: usize) -> StreamableReader<R> {
    StreamableReader {
        r,
        cap: capacity,
        buf: Vec::with_capacity(capacity),
    }
}

/// Make given read streamable.
pub struct StreamableReader<R> {
    r: R,
    cap: usize,
    buf: Vec<u8>,
}

impl<R: oio::Read> oio::Read for StreamableReader<R> {
    fn poll_read(&mut self, cx: &mut Context<'_>, buf: &mut [u8]) -> Poll<Result<usize>> {
        self.r.poll_read(cx, buf)
    }

    fn poll_seek(&mut self, cx: &mut Context<'_>, pos: SeekFrom) -> Poll<Result<u64>> {
        self.r.poll_seek(cx, pos)
    }

    fn poll_next(&mut self, cx: &mut Context<'_>) -> Poll<Option<Result<Bytes>>> {
        let dst = self.buf.spare_capacity_mut();
        let mut buf = ReadBuf::uninit(dst);
        unsafe { buf.assume_init(self.cap) };

        match ready!(self.r.poll_read(cx, buf.initialized_mut())) {
            Err(err) => Poll::Ready(Some(Err(err))),
            Ok(0) => Poll::Ready(None),
            Ok(n) => {
                buf.set_filled(n);
                Poll::Ready(Some(Ok(Bytes::from(buf.filled().to_vec()))))
            }
        }
    }
}

impl<R: oio::BlockingRead> oio::BlockingRead for StreamableReader<R> {
    fn read(&mut self, buf: &mut [u8]) -> Result<usize> {
        self.r.read(buf)
    }

    fn seek(&mut self, pos: SeekFrom) -> Result<u64> {
        self.r.seek(pos)
    }

    fn next(&mut self) -> Option<Result<Bytes>> {
        let dst = self.buf.spare_capacity_mut();
        let mut buf = ReadBuf::uninit(dst);
        unsafe { buf.assume_init(self.cap) };

        match self.r.read(buf.initialized_mut()) {
            Err(err) => Some(Err(err)),
            Ok(0) => None,
            Ok(n) => {
                buf.set_filled(n);
                Some(Ok(Bytes::from(buf.filled().to_vec())))
            }
        }
    }
}

#[cfg(test)]
mod tests {
    use bytes::BufMut;
    use bytes::BytesMut;
    use rand::prelude::*;

    use super::*;

    #[tokio::test]
    async fn test_into_stream() {
        use oio::ReadExt;

        let mut rng = ThreadRng::default();
        // Generate size between 1B..16MB.
        let size = rng.gen_range(1..16 * 1024 * 1024);
        let mut content = vec![0; size];
        rng.fill_bytes(&mut content);
        // Generate cap between 1B..1MB;
        let cap = rng.gen_range(1..1024 * 1024);

        let r = oio::Cursor::from(content.clone());
        let mut s = into_streamable_read(Box::new(r) as oio::Reader, cap);

        let mut bs = BytesMut::new();
        while let Some(b) = s.next().await {
            let b = b.expect("read must success");
            bs.put_slice(&b);
        }
        assert_eq!(bs.freeze().to_vec(), content)
    }

    #[test]
    fn test_into_stream_blocking() {
        use oio::BlockingRead;

        let mut rng = ThreadRng::default();
        // Generate size between 1B..16MB.
        let size = rng.gen_range(1..16 * 1024 * 1024);
        let mut content = vec![0; size];
        rng.fill_bytes(&mut content);
        // Generate cap between 1B..1MB;
        let cap = rng.gen_range(1..1024 * 1024);

        let r = oio::Cursor::from(content.clone());
        let mut s = into_streamable_read(Box::new(r) as oio::BlockingReader, cap);

        let mut bs = BytesMut::new();
        while let Some(b) = s.next() {
            let b = b.expect("read must success");
            bs.put_slice(&b);
        }
        assert_eq!(bs.freeze().to_vec(), content)
    }
}
