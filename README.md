# SQL Playground

A simple web application to upload CSV or SQL files and run SQL queries in a temporary SQLite database. Useful for quick experiments without installing any software.

## Setup

```bash
pip install -r requirements.txt
python app.py
```

Then open `http://localhost:5000` in your browser.

Use the **Show Plan** button to view SQLite's execution plan for a query. The output comes directly from `EXPLAIN QUERY PLAN` and is returned as JSON, not a graphical diagram. Example:

```
[
  {"id": 2, "parent": 0, "notused": 0, "detail": "SCAN chatlogs"}
]
```

Click **Visual Plan** to see a basic tree rendered from this JSON.
