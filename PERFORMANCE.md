# Performance Optimization Guide

## Overview
This document outlines performance optimizations implemented in the dcktools-metadata repository.

## JSON Structure Optimization

### Schema Validation
- **JSON Schema**: `meta.schema.json` provides fast validation without custom code
- **Strict Schema**: Uses `additionalProperties: false` to prevent bloat
- **Type Safety**: Enforces data types for efficient parsing

### File Size Optimization
- **Minimal Structure**: Only essential fields are included
- **No Redundancy**: Each field serves a specific purpose
- **Compact Formatting**: Uses minimal whitespace while maintaining readability

## Best Practices

### Updating metadata.json
1. **Batch Updates**: If making multiple changes, update once rather than multiple commits
2. **Timestamp Format**: Always use ISO 8601 format (YYYY-MM-DDTHH:mm:ssZ) for efficient parsing
3. **Validation**: Validate against schema before committing to catch errors early

### Web Serving Optimization
When serving this file over HTTP:
- Enable gzip compression (reduces size by ~60-70%)
- Set appropriate cache headers (e.g., `Cache-Control: public, max-age=3600`)
- Use ETags for conditional requests
- Consider CDN caching for global distribution

### Git Operations
- **Line Endings**: Consistent line endings prevent unnecessary diffs
- **Merge Strategy**: Use union merge for non-conflicting changes
- **Diff Driver**: JSON-specific diff for better change visibility

## Performance Metrics

### Current File Size
- Uncompressed: < 100 bytes
- Gzipped: < 80 bytes
- Parse time: < 1ms (typical JSON parser)

### Validation Performance
- Schema validation: O(1) complexity for this simple structure
- No external dependencies required for basic validation

## Future Optimizations

### If the file grows larger:
1. Consider splitting into multiple files by category
2. Implement pagination for large datasets
3. Use JSON streaming for very large files
4. Consider binary formats (e.g., MessagePack, CBOR) for extreme optimization

### Caching Strategy
For applications consuming this metadata:
1. Implement client-side caching with timestamp-based invalidation
2. Use HTTP conditional requests (If-Modified-Since)
3. Consider implementing a webhook for push-based updates instead of polling
