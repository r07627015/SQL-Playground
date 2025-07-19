from flask import Flask, request, render_template, jsonify
import sqlite3
import pandas as pd
import io
from sqlalchemy import text

app = Flask(__name__)

# In-memory SQLite database
conn = sqlite3.connect(':memory:', check_same_thread=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    if not file:
        return 'No file uploaded', 400

    filename = file.filename.lower()
    if filename.endswith('.csv'):
        df = pd.read_csv(file)
        table_name = request.form.get('table_name', 'data')
        df.to_sql(table_name, conn, if_exists='replace', index=False)
    elif filename.endswith('.sql'):
        sql_text = file.read().decode('utf-8')
        with conn:
            conn.executescript(sql_text)
    else:
        return 'Unsupported file type', 400

    return 'File processed successfully', 200

@app.route('/query', methods=['POST'])
def query():
    sql = request.form.get('sql')
    if not sql:
        return 'No query provided', 400
    try:
        df = pd.read_sql_query(sql, conn)
    except Exception as e:
        return jsonify({'error': str(e)})
    return df.to_json(orient='records')

if __name__ == '__main__':
    app.run(debug=True)
