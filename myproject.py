from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
@app.route('/list')
def showList():
    db = sqlite3.connect("listDB.db")
    db.row_factory = sqlite3.Row
    items = db.execute(
        'select name, address, total_price from Academy'
    ).fetchall()
    db.close()

    return render_template('list.html', items= items)


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)