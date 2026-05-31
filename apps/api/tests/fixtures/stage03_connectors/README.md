# Stage 03 Connector Fixtures

These JSON fixtures are the only default test inputs for Stage 03 source connectors.

They model metadata responses for OpenAlex, Crossref, Semantic Scholar, arXiv, and user-upload metadata. Tests must not call live provider APIs, require API keys, or depend on paid services. Fixture content is intentionally synthetic and only exercises provenance-preserving normalization into Stage 02 schema-compatible payloads.
