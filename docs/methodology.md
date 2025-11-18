# Methodology

## Objective
The AI Music Evaluation Benchmark is designed to provide a reproducible, genre-balanced dataset for assessing text-to-music generative systems. The dataset contains 450 prompts covering 150 genres (three prompts per genre).

## Prompt construction
- Prompts were authored to include: instrumentation, tempo suggestion (optional), production cues (e.g., "warm analog bass", "tight snares"), and structural expectations.
- Each prompt adheres to the schema defined in `/data/DATA_DICTIONARY.md`.

## Genre selection
- Genres were curated to cover cultural diversity (classical, folk, world, electronic subgenres) and production styles (lo-fi, hyperpop, orchestral).
- Selection criteria: representativeness, coverage across rhythmic/harmonic complexity, and production aesthetics.

## Validation
- Automated checks: ID continuity, genre counts, tempo ranges, keywords format, vocal flags.
- Human review: spot-checks for cultural sensitivity, ambiguous wording, and feasibility.

## Reproducibility
- All scripts necessary for validation and evaluation are provided in `/scripts`.
- Example notebook (`/notebooks/evaluation_pipeline.ipynb`) demonstrates pipeline usage.

## Limitations
See `/docs/limitations.md` for full discussion.
