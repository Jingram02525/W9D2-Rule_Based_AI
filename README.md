# W9D2 - AI Behaviors Without Models (Rule-Based Intelligence)

Quick start:

```
python -m venv .venv && source .venv/bin/activate
python -m pip install -r requirements.txt
python -m unittest -v
python src/app.py --name Team --time short --energy high
```

Decision Table Template:

| conditions | action |
|------------|--------|
| <fill>     | <fill> |
| DEFAULT    | <safe> |

Notes:
- Normalize inputs to lower-case and strip spaces.
- Add a guard clause for missing or invalid inputs.
