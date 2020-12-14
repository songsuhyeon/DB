from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
@app.route('/list')
def showList():
    db = sqlite3.connect("listDB.db")
    db.row_factory = sqlite3.Row
    items = db.execute(
        'select name, address, total_price'
        ' from list_item'
    ).fetchall()
    db.close()
    return render_template('list.html', items= items)

@app.route('/list/edit/<int:list_id>/')
def editList(list_id):
    db = sqlite3.connect("listDB.db")
    db.row_factory = sqlite3.Row
    item = db.execute(
        'select name, address, total_price'
        ' from list_item where id=?'
        ,(list_id,)
    ).fetchone()
    db.close()
    return render_template('editlist.html', item=item)


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)