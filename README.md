# SQL Playground

A simple web application to upload CSV or SQL files and run SQL queries in a temporary SQLite database. Useful for quick experiments without installing any software.

## Setup

```bash
pip install -r requirements.txt
python app.py
```

Then open `http://localhost:5000` in your browser.

Use the **Show Plan** button to view SQLite's execution plan for a query, similar to SSMS.
