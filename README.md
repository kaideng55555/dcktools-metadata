# DCKTools Metadata

A lightweight, high-performance metadata repository for DCKTools.

## Files

- `meta.json` - Core metadata file (< 100 bytes)
- `meta.schema.json` - JSON schema for validation
- `PERFORMANCE.md` - Performance optimization guide

## Quick Start

### Validate Metadata
```bash
# Using a JSON schema validator
npx ajv-cli validate -s meta.schema.json -d meta.json
```

### View Metadata
```bash
cat meta.json
```

## Performance Features

✅ **Minimal footprint**: < 100 bytes uncompressed  
✅ **Fast parsing**: < 1ms parse time  
✅ **Schema validation**: Efficient type checking  
✅ **Optimized for web serving**: Gzip-friendly structure  
✅ **Git optimized**: Proper line endings and merge strategies  

See [PERFORMANCE.md](PERFORMANCE.md) for detailed optimization guide.

## Schema

The metadata follows a strict JSON schema for:
- Fast validation without custom code
- Type safety and data integrity
- Prevention of unnecessary bloat

## Contributing

When updating metadata:
1. Validate against schema before committing
2. Use ISO 8601 format for timestamps
3. Keep structure minimal and efficient

## License

See repository license file.

