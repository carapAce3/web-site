from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

def connect_db():
    conn = sqlite3.connect('sql.db')
    cursor = conn.cursor()

    cursor.execute("SELECT menu, price FROM delivery")
    rows = cursor.fetchall()

    result = []
    for r in rows:
        dicrionary = {
            'menu': r[0],
            'price': r[1]
        }
        result.append(dicrionary)

    conn.close()
    return result

# Маршрут для відображення форми
@app.route('/')
def main_form():
    n = connect_db()
    return render_template('main.html', food = n)

@app.route('/menu')
def menu_form():
    n = connect_db()
    return render_template('menu.html')

@app.route('/delivery')
def delivery_form():
    return render_template('delivery.html')


if __name__ == '__main__':
    #app.run(debug=True)
    app.run(debug=True, host='0.0.0.0', port=5000)