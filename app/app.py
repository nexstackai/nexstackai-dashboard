import os
import psycopg2
from flask import Flask, render_template

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "database")
DB_NAME = os.getenv("DB_NAME", "dashboard")
DB_USER = os.getenv("DB_USER", "admin")
DB_PASSWORD = os.getenv("DB_PASSWORD", "example")


def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )


@app.route("/")
def dashboard():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT version, environment, status, deployed_at
        FROM deployments
        ORDER BY deployed_at DESC
        LIMIT 6;
    """)

    deployments = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "index.html",
        deployments=deployments,
        database_status="CONNECTED",
        application_status="HEALTHY"
    )


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)