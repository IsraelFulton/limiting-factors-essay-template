# Methods

## Data provenance
- List source tables and licenses
- Retrieval dates; version tags; DOIs (if any)

## Transformations
- Cleaning steps; instrument mapping (if applicable)
- FX/deflators and base-year
- File-level checksums (optional)

## Analysis
- Aggregations; uncertainty handling
- Figure-generation scripts and parameters

## Reproducibility
- `env/requirements.txt` with exact versions
- Deterministic seeds; pinned package versions
- End-to-end command: `make reproduce`
