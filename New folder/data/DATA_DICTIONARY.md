# Data Dictionary

Columns (final schema):
- **prompt_id**: Unique identifier in the format P001..P450.
- **genre**: Curated genre label (150 unique values, each appears exactly 3 times).
- **description**: Natural-language prompt describing instrumentation, production, and stylistic cues.
- **tempo**: Integer BPM (30-260) or blank when no strict tempo is required.
- **keywords**: 3–5 semicolon-separated short descriptors (no commas), e.g., `sitar;tabla;analog-bass`.
- **mood**: Short phrase describing intended emotional character, e.g., `nostalgic;serene`.
- **structure**: One of: loop, verse-chorus, build-drop, long_form, through-composed, ostinato, intro-build-drop, textural, atmospheric.
- **is_vocal**: `yes` or `no`.

Notes:
- Fields must not include unescaped newlines.
- Quoted fields are allowed for the description to include commas.
