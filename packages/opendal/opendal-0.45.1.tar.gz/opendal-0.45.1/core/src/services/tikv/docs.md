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
- [ ] scan
- [ ] ~~presign~~
- [ ] ~~blocking~~

## Configuration

- `endpoints`: Set the endpoints to the tikv cluster
- `insecure`: Set the insecure flag to the tikv cluster
- `ca_path`: Set the ca path to the tikv connection
- `cert_path`: Set the cert path to the tikv connection
- `key_path`: Set the key path to the tikv connection

You can refer to [`TiKVBuilder`]'s docs for more information

## Example

### Via Builder

```rust
use anyhow::Result;
use opendal::services::Tikv;
use opendal::Operator;

#[tokio::main]
async fn main() -> Result<()> {
    let mut builder = Tikv::default();
    builder.endpoints("127.0.0.1:2379");

    let op: Operator = Operator::new(builder)?.finish();
    Ok(())
}
```
