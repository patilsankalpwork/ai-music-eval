# Scripts

- validate_dataset.py: Validate the prompt CSV schema and basic content rules.
- evaluate_model.py: Template to compute automated metrics on generated WAVs.
- analyze_results.py: Aggregate rater composite scores and compute basic statistics.

Usage:
python3 scripts/validate_dataset.py data/prompts_converted.csv
python3 scripts/evaluate_model.py /path/to/generated_wavs
python3 scripts/analyze_results.py evaluation/rater_sheet_template.csv
