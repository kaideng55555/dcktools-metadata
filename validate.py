#!/usr/bin/env python3
"""
Fast JSON metadata validator for dcktools-metadata

This script provides efficient validation of meta.json against the schema.
Uses Python's built-in json module for fast parsing (C-optimized).
"""

import json
import sys
from pathlib import Path


def validate_meta_json():
    """Validate meta.json structure and content efficiently."""
    
    try:
        # Read meta.json - using Path for efficient file operations
        meta_path = Path(__file__).parent / 'meta.json'
        
        # Parse JSON - Python's json.loads is C-optimized for speed
        with meta_path.open('r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Basic validation (fast, no external dependencies)
        errors = []
        
        # Check required fields
        required_fields = ['name', 'updated']
        for field in required_fields:
            if field not in data:
                errors.append(f"Missing required field: {field}")
        
        # Validate field types
        if 'name' in data:
            if not isinstance(data['name'], str):
                errors.append("Field 'name' must be a string")
            elif len(data['name']) == 0:
                errors.append("Field 'name' cannot be empty")
            elif len(data['name']) > 100:
                errors.append("Field 'name' exceeds maximum length of 100")
        
        if 'updated' in data:
            if not isinstance(data['updated'], str):
                errors.append("Field 'updated' must be a string")
            else:
                # Basic ISO 8601 format check (fast regex-free validation)
                updated = data['updated']
                if not (len(updated) >= 20 and 'T' in updated and 'Z' in updated):
                    errors.append("Field 'updated' must be in ISO 8601 format (YYYY-MM-DDTHH:mm:ssZ)")
        
        # Check for unexpected fields (prevents bloat)
        allowed_fields = set(required_fields)
        extra_fields = set(data.keys()) - allowed_fields
        if extra_fields:
            errors.append(f"Unexpected fields found: {', '.join(extra_fields)}")
        
        # Report results
        if errors:
            print("❌ Validation failed:")
            for error in errors:
                print(f"  - {error}")
            return False
        else:
            print("✅ Validation passed!")
            print(f"  - File size: {meta_path.stat().st_size} bytes")
            print(f"  - Fields: {len(data)}")
            return True
            
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON: {e}")
        return False
    except FileNotFoundError:
        print("❌ File meta.json not found")
        return False
    except Exception as e:
        print(f"❌ Validation error: {e}")
        return False


if __name__ == '__main__':
    success = validate_meta_json()
    sys.exit(0 if success else 1)
