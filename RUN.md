# How to Run Frontend and Backend

## Backend (FastAPI)

### 1. Activate your conda environment
```bash
conda activate kv_billing
```

### 2. Navigate to project root
```bash
cd /Users/benedikt/Downloads/kv_billing_mvp
```

### 3. Start the FastAPI server
```bash
uvicorn app.main:app --reload
```

The backend will run on: **http://localhost:8000**

You can test it at: **http://localhost:8000/docs** (FastAPI Swagger UI)

---

## Frontend (React/Vite)

### 1. Navigate to frontend directory
```bash
cd /Users/benedikt/Downloads/kv_billing_mvp/praxis-doc-aid
```

### 2. Install dependencies (first time only)
```bash
npm install
```

### 3. Start the development server
```bash
npm run dev
```

The frontend will run on: **http://localhost:5173** (or another port if 5173 is taken)

---

## Running Both Together

You need **two terminal windows/tabs**:

**Terminal 1 (Backend):**
```bash
conda activate kv_billing
cd /Users/benedikt/Downloads/kv_billing_mvp
uvicorn app.main:app --reload
```

**Terminal 2 (Frontend):**
```bash
cd /Users/benedikt/Downloads/kv_billing_mvp/praxis-doc-aid
npm run dev
```

Then open your browser to: **http://localhost:5173**

---

## Troubleshooting

- **Backend port conflict?** Change port: `uvicorn app.main:app --reload --port 8001`
- **Frontend port conflict?** Vite will automatically use the next available port
- **CORS errors?** Make sure backend is running first, then start frontend
- **Import errors in backend?** Make sure you're running from project root: `uvicorn app.main:app` (not `uvicorn main:app`)

