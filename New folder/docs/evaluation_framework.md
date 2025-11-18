# Evaluation Framework

## Objectives
Evaluate models across multiple axes:
- Genre recognition accuracy
- Timbre fidelity
- Rhythmic adaptation
- Structural correctness
- Melodic/harmonic correctness
- Production aesthetic
- Cultural fidelity
- Vocal handling (where applicable)

## Scoring
Use per-prompt human rater scores (0-5 integers) across each metric. See `/evaluation/scoring_rubric.csv` for weightings.

Composite score = sum(metric_score * weight).

## Automated metrics (recommended)
- Tempo detection (BPM) vs prompt tempo
- Chord recognition / key estimation
- Spectral similarity / timbre fingerprinting (MFCC-based)
- Loudness & dynamic range checks
- Voice activity detection for `is_vocal=yes`

## Evaluation procedure
1. Generate audio outputs for each prompt (specify model checkpoint and inference settings).
2. Normalize audio length and loudness.
3. Run automated metrics.
4. Collect human ratings using `rater_sheet_template.csv`.
5. Aggregate results using `scripts/analyze_results.py`.

## Rater protocol
- Minimum 3 independent raters per prompt.
- Raters must be neutral and, where possible, have music background.
- Collect free-text comments for edge cases.

