# Webhook Receiver – Customized Solution 🌟

This repo is a **complete solution** for the Techstax Developer Assessment:

* Receives **GitHub webhooks** for `push`, `pull_request` (open/merge).
* Saves a **human‑readable message** in **MongoDB**.
* Simple UI polls every 15 seconds and shows latest events.

---

## 🔧 Setup (Local)

```bash
git clone <this‑repo>
cd custom-webhook-repo

python3 -m venv venv
source venv/bin/activate          # `venv\Scripts\activate` on Windows
pip install -r requirements.txt

# If you use MongoDB Atlas set env var:
export MONGO_URI="mongodb+srv://<user>:<pass>@cluster0.example.mongodb.net/webhook_db?retryWrites=true&w=majority"

python run.py
```

* Server runs on **http://127.0.0.1:5000/**
* Webhook endpoint: **POST http://127.0.0.1:5000/webhook/receiver**

---

## 🚀 Deploy

Any host that supports Python (Render, Railway, Heroku, Fly.io).  
Just set `MONGO_URI` environment variable.

---

## 🖥️ Frontend Demo

Open `http://localhost:5000/` and push / PR / merge in your GitHub repo — you’ll see messages appear every 15 s.
