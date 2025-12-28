from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route("/")
def healthcheck():
    try:
        conn = psycopg2.connect(
            user=os.getenv("user"),
            password=os.getenv("password"),
            host=os.getenv("host"),
            port=os.getenv("port"),
            dbname=os.getenv("dbname")
        )
        cur = conn.cursor()
        cur.execute("SELECT NOW();")
        now = cur.fetchone()
        cur.close()
        conn.close()
        return {
            "status": "connected",
            "time": str(now)
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)