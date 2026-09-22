# Codomax Module 5 - Python Application Development (Advanced)

## Project Overview
Fully documented Python REST API built with Flask + SQLite, including Authentication, Validation, CRUD, and Analytics.

This is an upgraded version of Module 4 with:
- Flask fundamentals, routing, endpoints
- SQLite database integration & CRUD using SQL
- API Authentication (API Key)
- Schema validation & error handling
- Endpoint testing & documentation

## Live Links
- **GitHub:** https://github.com/nafris565-cmyk/codomax-module-5-python-api
- **Live API Docs:** /api/docs
- **Base URL (when deployed):** https://your-app.onrender.com

## Tech Stack
- Python 3.10, Flask 2.3.3
- SQLite (file-based)
- Gunicorn for production

## Setup Locally
```bash
pip install -r requirements.txt
python app.py
```
Visit: http://localhost:5000

## API Documentation

### Authentication
For POST/PUT/DELETE, add header:
```
X-API-KEY: codomax_2025_secret_key
```

### Endpoints

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| GET | / | No | API info |
| GET | /api/docs | No | Full docs |
| GET | /api/health | No | Health check |
| GET | /api/products | No | List products ?category= & min_price= |
| GET | /api/products/<id> | No | Get one |
| POST | /api/products | Yes | Create |
| PUT | /api/products/<id> | Yes | Update |
| DELETE | /api/products/<id> | Yes | Delete |
| GET | /api/analytics | No | Analytics |

### Sample Requests

**Create Product:**
```json
POST /api/products
Headers: X-API-KEY: codomax_2025_secret_key
{
  "name": "MacBook Pro",
  "category": "Electronics",
  "price": 2499.99,
  "stock": 10,
  "description": "M3 Chip"
}
```

## Testing
Run `python test_api.py` to test endpoints.

## Learning Notes
See LEARNING_NOTES.md or Google Docs link for detailed notes.

## Author
Nafri Nafri - CDS_INT_202693138
Codomax Internship - Module 5
