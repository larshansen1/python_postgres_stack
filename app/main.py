from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_record():
    try:
        conn = psycopg2.connect(os.getenv("DATABASE_URL"))
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, description FROM mytable LIMIT 1;")
        record = cursor.fetchone()
        cursor.close()
        conn.close()
        return {"id": record[0], "name": record[1], "description": record[2]}
    except Exception as e:
        return str(e)

@app.route('/')
def home():
    record = get_record()
    return jsonify(record=record)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

