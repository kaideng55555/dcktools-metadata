.PHONY: validate check help

# Default target
help:
	@echo "Available targets:"
	@echo "  validate  - Validate meta.json against schema (fast)"
	@echo "  check     - Run all checks"
	@echo "  help      - Show this help message"

# Fast validation using Python (no external dependencies)
validate:
	@python3 validate.py

# Run all checks
check: validate
	@echo "All checks passed!"
