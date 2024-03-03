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

use std::fmt::Display;
use std::fmt::Formatter;

/// Operation is the name for APIs in `Accessor`.
#[derive(Debug, Copy, Clone, Hash, Eq, PartialEq, Default)]
#[non_exhaustive]
pub enum Operation {
    /// Operation for [`crate::raw::Accessor::info`]
    #[default]
    Info,
    /// Operation for [`crate::raw::Accessor::create_dir`]
    CreateDir,
    /// Operation for [`crate::raw::Accessor::read`]
    Read,
    /// Operation for [`crate::raw::Accessor::write`]
    Write,
    /// Operation for [`crate::raw::Accessor::copy`]
    Copy,
    /// Operation for [`crate::raw::Accessor::rename`]
    Rename,
    /// Operation for [`crate::raw::Accessor::stat`]
    Stat,
    /// Operation for [`crate::raw::Accessor::delete`]
    Delete,
    /// Operation for [`crate::raw::Accessor::list`]
    List,
    /// Operation for [`crate::raw::Accessor::batch`]
    Batch,
    /// Operation for [`crate::raw::Accessor::presign`]
    Presign,
    /// Operation for [`crate::raw::Accessor::blocking_create_dir`]
    BlockingCreateDir,
    /// Operation for [`crate::raw::Accessor::blocking_read`]
    BlockingRead,
    /// Operation for [`crate::raw::Accessor::blocking_write`]
    BlockingWrite,
    /// Operation for [`crate::raw::Accessor::blocking_copy`]
    BlockingCopy,
    /// Operation for [`crate::raw::Accessor::blocking_rename`]
    BlockingRename,
    /// Operation for [`crate::raw::Accessor::blocking_stat`]
    BlockingStat,
    /// Operation for [`crate::raw::Accessor::blocking_delete`]
    BlockingDelete,
    /// Operation for [`crate::raw::Accessor::blocking_list`]
    BlockingList,
}

impl Operation {
    /// Convert self into static str.
    pub fn into_static(self) -> &'static str {
        self.into()
    }
}

impl Display for Operation {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        write!(f, "{}", self.into_static())
    }
}

impl From<Operation> for &'static str {
    fn from(v: Operation) -> &'static str {
        match v {
            Operation::Info => "metadata",
            Operation::CreateDir => "create_dir",
            Operation::Read => "read",
            Operation::Write => "write",
            Operation::Copy => "copy",
            Operation::Rename => "rename",
            Operation::Stat => "stat",
            Operation::Delete => "delete",
            Operation::List => "list",
            Operation::Presign => "presign",
            Operation::Batch => "batch",
            Operation::BlockingCreateDir => "blocking_create_dir",
            Operation::BlockingRead => "blocking_read",
            Operation::BlockingWrite => "blocking_write",
            Operation::BlockingCopy => "blocking_copy",
            Operation::BlockingRename => "blocking_rename",
            Operation::BlockingStat => "blocking_stat",
            Operation::BlockingDelete => "blocking_delete",
            Operation::BlockingList => "blocking_list",
        }
    }
}

impl From<Operation> for String {
    fn from(v: Operation) -> Self {
        v.into_static().to_string()
    }
}
