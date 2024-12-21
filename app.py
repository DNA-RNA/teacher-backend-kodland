from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Veritabanı bağlantısı
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Ana sayfa
@app.route("/")
def home():
    return render_template("home.html")

# Quiz sayfası
@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    conn = get_db_connection()
    questions = conn.execute("SELECT * FROM questions").fetchall()

    # En yüksek skoru al
    best_score = conn.execute("SELECT MAX(high_score) AS max_score FROM students").fetchone()["max_score"]
    if best_score is None:
        best_score = 0  # Eğer skor yoksa 0 gösterilsin

    conn.close()

    if request.method == "POST":
        user_answers = request.form
        username = user_answers.get("username")
        score = calculate_score(user_answers, questions)

        # Kullanıcı skorunu veritabanına kaydet
        conn = get_db_connection()
        conn.execute(
            "INSERT INTO students (username, high_score) VALUES (?, ?)",
            (username, score)
        )
        conn.commit()
        conn.close()

        # Sonuç sayfasına yönlendirme
        return redirect(url_for("quiz"))

    return render_template("quiz.html", questions=questions, best_score=best_score)

# Puan hesaplama
def calculate_score(user_answers, questions):
    score = 0
    for question in questions:
        question_id = f"question{question['id']}"
        user_answer = user_answers.get(question_id)
        if user_answer == question["correct_answer"]:
            score += 1
    total_questions = len(questions)
    return int((score / total_questions) * 100)

# Ana fonksiyon
if __name__ == "__main__":
    app.run(debug=True)
