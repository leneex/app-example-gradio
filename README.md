# Gradio

Example [Gradio](https://www.gradio.app/) app. Gradio is a Python library for building web interfaces to machine learning models and AI apps, widely used on Hugging Face Spaces.

## Deploy settings

| Field | Value |
| --- | --- |
| Build | Railpack |
| Project directory | `/` |
| Install command | leave empty |
| Build command | leave empty |
| Start command | leave empty |
| Application port | `7860` |
| Health check path | `/` |

## <a name="dev"></a>Run locally

```bash
# create virtual environment and install dependencies
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

# start the app
python3 app.py
```

The app opens at http://localhost:7860.

Requires Python 3.10–3.13 — these versions are officially supported by Gradio.
