from flask import Flask, render_template, request, redirect, url_for
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

@app.route('/list/edit/<int:list_name>/', methods=['GET','POST'])
def editList(list_name):
    if request.method=='POST':
        db = sqlite3.connect("listDB.db")
        db.row_factory = sqlite3.Row
        db.execute(
            'update Academy'
            ' set name=?'
            ' where name=?',
            (request.form['list_name'],list_name)
        )
        db.commit()
        db.close()
        return redirect(url_for('showlist'))
    else:
        db = sqlite3.connect("listDB.db")
        db.row_factory = sqlite3.Row
        item = db.execute(
            'select name, address, total_price from Academy where name=?',(list_name,)
        ).fetchone()
        db.close()
        return render_template('editlist.html', item=item)


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)