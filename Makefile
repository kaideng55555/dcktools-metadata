.PHONY: validate check publish help

# Default target
help:
	@echo "Available targets:"
	@echo "  validate  - Validate meta.json against schema (fast)"
	@echo "  check     - Run all checks"
	@echo "  publish   - Validate, then publish metadata to Solana"
	@echo "  help      - Show this help message"

# Fast validation using Python (no external dependencies)
validate:
	@echo "🔍 Validating meta.json..."
	@python3 validate.py

# Run all checks
check: validate
	@echo "✅ All checks passed!"

# Publish validated metadata to Solana using Metaplex CLI
publish: check
	@echo "🚀 Publishing metadata to Solana..."
	@npx --yes github:metaplex-foundation/mplx@main core asset update \
		6yFZK7HkP1eG8r9zWmJ2Z8rU1zTgLjP1fUvzLqfYuhyA \
		--json meta.json \
		--keypair ~/dckmints.json \
		--log-level info || (echo "❌ Publish failed" && exit 1)
	@echo "✅ Metadata successfully updated on-chain!"
