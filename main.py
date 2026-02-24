from flask import Flask, render_template, request, redirect, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "skill2income_secret"

def init_db():
    conn = sqlite3.connect("skill2income.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            skill TEXT,
            time TEXT,
            goal INTEGER,
            income INTEGER DEFAULT 0,
            streak INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        skill = request.form["skill"]
        time = request.form["time"]
        goal = request.form["goal"]

        conn = sqlite3.connect("skill2income.db")
        c = conn.cursor()
        c.execute("INSERT INTO users (name, skill, time, goal) VALUES (?, ?, ?, ?)",
                  (name, skill, time, goal))
        conn.commit()
        user_id = c.lastrowid
        conn.close()

        session["user_id"] = user_id
        return redirect("/dashboard")

    return render_template("index.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    user_id = session.get("user_id")

    if not user_id:
        return redirect("/")

    conn = sqlite3.connect("skill2income.db")
    c = conn.cursor()

    if request.method == "POST":
        add_income = int(request.form["income"])
        c.execute("UPDATE users SET income = income + ?, streak = streak + 1 WHERE id = ?",
                  (add_income, user_id))
        conn.commit()

    c.execute("SELECT name, skill, time, goal, income, streak FROM users WHERE id = ?", (user_id,))
    user = c.fetchone()
    conn.close()

    return render_template("dashboard.html", user=user)

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
