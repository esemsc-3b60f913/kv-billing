# Deployment Guide

## Overview
- **Backend**: FastAPI (Python)
- **Frontend**: React/Vite (built with Lovable)

## Deployment Options

### Option 1: Render (Recommended - Easiest) ⭐

**Backend on Render:**
1. Go to [render.com](https://render.com) and sign up
2. Create a new **Web Service**
3. Connect your GitHub repo
4. Settings:
   - **Name**: `kv-billing-backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: Leave empty (Render will automatically use `Procfile`)
   - **Root Directory**: `/` (leave empty or set to root)
   
   **Note**: If you manually set Start Command, use: `uvicorn app.main:app --host 0.0.0.0 --port $PORT` (no backticks, no extra quotes)
5. Add environment variables:
   - `OPENAI_API_KEY`: Your OpenAI API key
6. Deploy!

**Frontend on Render:**
1. Create a new **Static Site** on Render
2. Connect your GitHub repo
3. Settings:
   - **Root Directory**: `/praxis-doc-aid`
   - **Build Command**: `npm install && npm run build`
   - **Publish Directory**: `dist`
4. Add environment variable:
   - `VITE_API_URL`: `https://your-backend-url.onrender.com`
5. Deploy!

---

### Option 2: Railway (Very Easy)

**Backend on Railway:**
1. Go to [railway.app](https://railway.app) and sign up
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repo
4. Railway auto-detects Python → Click "Deploy"
5. Add environment variable: `OPENAI_API_KEY`
6. Get your backend URL (e.g., `https://kv-billing.up.railway.app`)

**Frontend on Railway or Vercel:**
- Same as Render frontend steps, but use Railway's static site or Vercel

---

### Option 3: Vercel (Frontend) + Render/Railway (Backend)

**Backend**: Same as Option 1 or 2 above

**Frontend on Vercel:**
1. Go to [vercel.com](https://vercel.com) and sign up
2. Click "Add New Project"
3. Import your GitHub repo
4. Settings:
   - **Framework Preset**: Vite
   - **Root Directory**: `praxis-doc-aid`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
5. Add environment variable:
   - `VITE_API_URL`: Your backend URL
6. Deploy!

---

### Option 4: Lovable Deployment (If Available)

If Lovable has built-in deployment:
1. Check Lovable dashboard for "Deploy" button
2. It might auto-deploy or give you a Vercel/Netlify option
3. Update `VITE_API_URL` to point to your deployed backend

---

## Required Setup Before Deployment

### 1. Update CORS in Backend

Edit `app/main.py` to allow your frontend domain:

```python
# Update this line in main.py
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Keep for local dev
        "https://your-frontend-domain.vercel.app",  # Your deployed frontend
        "https://your-frontend-domain.netlify.app",  # Alternative
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### 2. Create Production Environment File

Create `.env` file in the backend root (for Render/Railway):

```
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. Update Frontend API URL

In `praxis-doc-aid/.env.production`:

```
VITE_API_URL=https://your-backend-url.onrender.com
```

Or create `.env.production.local`:

```
VITE_API_URL=https://your-backend-url.onrender.com
```

### 4. Fix Backend Import Issue

Create a `Procfile` in the backend root (for Render):

```
web: uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

Or for Railway, create `railway.json`:

```json
{
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "uvicorn app.main:app --host 0.0.0.0 --port $PORT"
  }
}
```

### 5. Add Missing Dependencies

Your `requirements.txt` might be missing `requests` and `openai`. Update it:

```txt
fastapi==0.115.0
uvicorn==0.30.6
pydantic==2.9.2
python-dotenv==1.0.1
requests==2.31.0
openai==1.12.0
```

---

## Quick Deployment Checklist

### Backend:
- [ ] Add `requests` and `openai` to `requirements.txt`
- [ ] Update CORS to include frontend domain
- [ ] Set `OPENAI_API_KEY` environment variable on platform
- [ ] Deploy and get backend URL

### Frontend:
- [ ] Update `VITE_API_URL` environment variable
- [ ] Build and deploy
- [ ] Test API connection

---

## Recommended: Render for Both (Simplest)

1. **Backend**: Render Web Service (Free tier available)
2. **Frontend**: Render Static Site (Free tier available)
3. Both can be from same GitHub repo, just different services

**Pros:**
- Free tier available
- Easy setup
- Automatic SSL certificates
- Same platform for both

---

## Troubleshooting

### Backend won't start:
- Check if `uvicorn` command is correct
- Verify `app.main:app` import path
- Check environment variables are set

### Frontend can't reach backend:
- Verify `VITE_API_URL` is set correctly
- Check CORS settings in backend
- Ensure backend is running and accessible

### Import errors in backend:
- Make sure you're running from project root
- Command should be `uvicorn app.main:app` (not `uvicorn main:app`)

---

## Estimated Deployment Time

- **Backend**: 10-15 minutes (Render/Railway)
- **Frontend**: 5-10 minutes (Vercel/Netlify)
- **Total**: ~20-30 minutes

---

## Free Tier Limits

- **Render**: Free tier with limitations (may sleep after inactivity)
- **Railway**: $5/month credit (generous free tier)
- **Vercel**: Free tier for frontend (very generous)

For production use, consider upgrading to paid plans for:
- No sleep/startup delays
- More resources
- Custom domains

