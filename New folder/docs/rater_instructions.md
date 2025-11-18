# Rater Instructions

## Overview
Raters assess generated audio against the textual prompt across defined metrics. Use 0-5 integer scores.

## Metrics
- **Genre recognition**: 5 = indistinguishable; 0 = totally wrong.
- **Timbre fidelity**: Are the named instruments/timbres present?
- **Rhythmic adaptation**: Tempo and groove correctness.
- **Structural correctness**: Does structure match prompt (loop / verse-chorus / drop etc.)?
- **Melodic/harmonic correctness**: Key center, melodies present.
- **Production aesthetic**: Mixing, panning, reverb, saturation.
- **Cultural fidelity**: Respectful and idiomatic use of cultural elements.
- **Vocal handling**: If `is_vocal=yes`, evaluate lyrics placement, intelligibility, timbre.

## Practical steps
- Use headphones in a quiet environment.
- Listen at least twice: one for global impression, one for detailed scoring.
- When in doubt, discuss with other raters (for arbitration).

## Logging
- Use `rater_sheet_template.csv` to log scores.
- Add comments for any unusual artifacts or cultural concerns.
