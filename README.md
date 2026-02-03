# 💊 AI-HCP-CRM — Medicine World CRM

An **AI-powered Healthcare Professional (HCP) CRM system** built with:

* **Backend:** FastAPI
* **Frontend:** Streamlit (Dark Theme, Medical UI)
* **AI Agents:** Summarization & Sentiment Analysis
* **Database:** SQL-based persistence
* **Use Case:** Managing doctors, logging interactions, and tracking follow-ups

---

## 🚀 Features

### ✅ HCP Management

* View all doctors (HCPs)
* Add new HCP profiles
* Fetch interaction history of any doctor

### ✅ Interaction Management

* Log new interactions with doctors
* Auto-generate **summary + sentiment**
* Store follow-up actions
* Edit previous interactions
* View all interactions in dashboard style

### 🎨 Frontend (Streamlit)

* Dark medical theme
* Background medical image
* Card-based UI
* Dashboard with statistics
* Clean forms and tables

---

## 📁 Project Structure

```
ai-hcp-crm/
│
├── backend/
│   ├── main.py
│   ├── routers/
│   ├── agents/
│   ├── tools/
│   ├── services/
│   ├── models/
│   ├── schemas/
│   └── database/
│
├── frontend/
│   ├── app.py
│   └── requirements.txt
│
└── README.md
```

---

## 🛠️ Tech Stack

| Layer    | Technology                       |
| -------- | -------------------------------- |
| Backend  | FastAPI                          |
| Frontend | Streamlit                        |
| AI       | LLM-based summarizer + sentiment |
| Database | SQL                              |
| Language | Python                           |

---

## ▶️ How to Run the Project

### 1️⃣ Run Backend

```bash
cd backend
uvicorn main:app --reload
```

Backend will run at:

```
http://127.0.0.1:8000
```

You can test APIs at:

```
http://127.0.0.1:8000/docs
```

---

### 2️⃣ Run Frontend

```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

Frontend will open at:

```
http://localhost:8501
```

---

## 🔌 API Endpoints Used in Frontend

### HCP APIs

| Method | Endpoint                | Description             |
| ------ | ----------------------- | ----------------------- |
| GET    | `/hcp/`                 | Get all doctors         |
| POST   | `/hcp/`                 | Add new doctor          |
| GET    | `/hcp/{hcp_id}/history` | Get interaction history |

### Interaction APIs

| Method | Endpoint                  | Description          |
| ------ | ------------------------- | -------------------- |
| POST   | `/interactions/log`       | Log interaction      |
| GET    | `/interactions/`          | Get all interactions |
| PUT    | `/interactions/edit/{id}` | Edit interaction     |

---

## 📌 Example Interaction Payload

```json
{
  "hcp_id": 104,
  "raw_text": "Discussion about vaccination updates",
  "follow_up": "Send updated schedule"
}
```

---

## 🎯 Purpose of Project

This system is designed for:

* Medical representatives
* Pharma companies
* Hospitals
* Healthcare CRM teams

It helps in **tracking doctor interactions intelligently using AI.**

---

## 👨‍💻 Developed By

**Suryakanta Barik**
Integrated MCA | AI/ML | Data Analytics | FastAPI | Streamlit

---

If you want, I can also:

* add **screenshots section**,
* add **deployment steps**, or
* format this with **badges** (FastAPI, Streamlit, Python, etc.).
