from flask import Flask, jsonify
import sqlite3, os

app = Flask(__name__)

SALES_DATA = [
    {"id": 1, "product": "Laptop", "category": "Electronics", "price": 1200, "quantity": 5, "date": "2025-05-01"},
    {"id": 2, "product": "Mobile", "category": "Electronics", "price": 800, "quantity": 10, "date": "2025-05-02"},
    {"id": 3, "product": "Shirt", "category": "Fashion", "price": 40, "quantity": 20, "date": "2025-05-03"},
]

def init_db():
    conn = sqlite3.connect('sales.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS sales (id INTEGER PRIMARY KEY, product TEXT, category TEXT, price REAL, quantity INTEGER, date TEXT)")
    c.execute("DELETE FROM sales")
    for item in SALES_DATA:
        c.execute("INSERT INTO sales VALUES (?,?,?,?,?,?)", (item['id'], item['product'], item['category'], item['price'], item['quantity'], item['date']))
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return jsonify({
        "message": "Codomax Module 4 - Nafri CDS/INT/202693138 - LIVE!",
        "endpoints": ["/api/sales", "/api/analytics"],
        "status": "Running"
    })

@app.route('/api/sales')
def get_sales():
    conn = sqlite3.connect('sales.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM sales")
    rows = [dict(row) for row in c.fetchall()]
    conn.close()
    return jsonify(rows)

@app.route('/api/analytics')
def analytics():
    conn = sqlite3.connect('sales.db')
    c = conn.cursor()
    c.execute("SELECT category, SUM(price*quantity) as revenue FROM sales GROUP BY category")
    data = [{"category": r[0], "revenue": r[1]} for r in c.fetchall()]
    c.execute("SELECT SUM(price*quantity) FROM sales")
    total = c.fetchone()[0]
    conn.close()
    return jsonify({"total_revenue": total, "by_category": data})

init_db()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
