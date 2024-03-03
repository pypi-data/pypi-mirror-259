## Capabilities

This service can be used to:

- [x] stat
- [x] read
- [x] write
- [x] create_dir
- [x] delete
- [x] copy
- [x] rename
- [ ] ~~list~~
- [x] scan
- [ ] ~~presign~~
- [x] blocking

## Configuration

- `datadir`: Set the path to the sled data directory

You can refer to [`SledBuilder`]'s docs for more information

## Example

### Via Builder

```rust
use anyhow::Result;
use opendal::services::Sled;
use opendal::Operator;

#[tokio::main]
async fn main() -> Result<()> {
    let mut builder = Sled::default();
    builder.datadir("/tmp/opendal/sled");

    let op: Operator = Operator::new(builder)?.finish();
    Ok(())
}
```
