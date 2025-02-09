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


@app.route('/submit', methods=['POST'])
def submit_form():
    review = request.form['review']
    
    with sqlite3.connect("database2.db") as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO savings (review) VALUES (?)', (review,))
        conn.commit()
    
    return redirect("/")

@app.route('/submit2', methods=['POST'])
def submit2_form():
    place = request.form['place']
    card = request.form['card']
    date = request.form['date']
    cvv = request.form['cvv']
    food = request.form['food']
    
    with sqlite3.connect("database2.db") as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO ooo (delivery, card, date, CVV, food) VALUES (?,?,?,?,?)', (place, card, date, cvv, food))
        conn.commit()
    
    return redirect("/")


if __name__ == '__main__':
    #app.run(debug=True)
    app.run(debug=True, host='0.0.0.0', port=5000)

# https://carapacee.pythonanywhere.com/