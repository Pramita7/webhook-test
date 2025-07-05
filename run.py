import os
from app import create_app

app = create_app()

if __name__ == "__main__":
    # In production use gunicorn/uwsgi instead of built‑in server
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT",5000)))
