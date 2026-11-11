# Render cloud server starter

This repository includes a tiny Python web server that you can deploy on Render. It has a welcome page at `/` and a health check at `/health`.

## Deploy on Render

1. Push or commit these files to your GitHub repository.
2. In Render, choose **New +** → **Blueprint** and connect this repository.
3. Render reads `render.yaml`; review the settings and create the service.
4. When deployment finishes, open the service URL. You should see the welcome page.

You can also create a **Web Service** manually with:

- **Runtime:** Python
- **Build command:** `pip install -r requirements.txt`
- **Start command:** `gunicorn app:app --bind 0.0.0.0:$PORT`

Render supplies the `PORT` environment variable. The app binds to it and exposes `/health` for status checks. This is a starter only; it does not persist data between restarts.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Then visit `http://localhost:10000`.
