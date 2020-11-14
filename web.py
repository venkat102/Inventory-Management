from flask import Flask as f, render_template as rt, request as rq, redirect
from flask_sqlalchemy import SQLAlchemy as sa
from datetime import datetime

app = f(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'

db = sa(app)

class product_tbl(db.Model):
    pid = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(50), nullable=False)
    plid = db.Column(db.Integer, nullable=False)
    plname = db.Column(db.String(50), nullable=False)
    pqty = db.Column(db.Integer, nullable=False)
    pr = db.Column(db.Integer, nullable=False)


class location_tbl(db.Model):
    loid = db.Column(db.Integer, primary_key=True)
    loc = db.Column(db.String(50), nullable=False)
    loname = db.Column(db.Integer, nullable=False)
    lad = db.Column(db.Text, nullable=False)


class productmovement_tbl(db.Model):
    mid = db.Column(db.Integer, primary_key=True)
    mtime = db.Column(db.DateTime, default=datetime.now)
    mfrom = db.Column(db.Text, nullable=False)
    mto = db.Column(db.Text, nullable=False)
    mprod = db.Column(db.String(50), nullable=False)
    mqty = db.Column(db.Integer, nullable=False)


@app.route('/inventory')
@app.route('/')
def inventory():return rt("Inventory.html", products = product_tbl.query.all())


@app.route('/product',methods=['GET','POST'])
def product():
    if rq.method == 'POST':
        new_product = product_tbl(pid= rq.form['pid'], pname= rq.form['pname'], plid=rq.form['plid'], plname=rq.form['plname'], pqty=rq.form['pqty'], pr= rq.form['pprice'])
        db.session.add(new_product)
        db.session.commit()
        return redirect('/product')
    else:return rt("Product.html", products = product_tbl.query.all())

@app.route('/location',methods=['GET','POST'])
def location():
    if rq.method == 'POST':
        new_location = location_tbl(loid= rq.form['lid'], loc= rq.form['lloc'], loname=rq.form['lname'], lad=rq.form['ladd'])
        db.session.add(new_location)
        db.session.commit()
        return redirect('/location')
    else:return rt("Location.html", products = location_tbl.query.all())

@app.route('/productmovement',methods=['GET','POST'])
def productmovement():
    if rq.method == 'POST':
        new_movement = productmovement_tbl(mid= rq.form['mpid'],mfrom= rq.form['mfrom'], mto=rq.form['mto'], mprod=rq.form['mproduct'], mqty=rq.form['mqty'])
        db.session.add(new_movement)
        db.session.commit()
        return redirect('/productmovement')
    else:return rt("Product Movement.html", products = productmovement_tbl.query.all())


if __name__=="__main__":
    app.run(debug=True)
'''{% for content in %}
    <tr>
    <td>{{}}</td>
    <td>{{}}</td>
    <td>{{}}</td>
    <td>{{}}</td>
    <td>{{}}</td>
  </tr>
    {% endfor %}'''
