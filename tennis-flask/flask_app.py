from flask import Flask
from flask.json import jsonify
import pymysql

app = Flask(__name__)
db = pymysql.connect(
    host="DESKTOP-I2KTJTT",
    user="public",
    passwd="@Password1",
    db="tennis_raquets"
)

cur = db.cursor()

@app.route('/')
def greet():
    return "<h1>Hello there!<h1>"

@app.route('/brand/all')
def get_raquets():
    sql = "SELECT DISTINCT brand FROM raquets"
    cur.execute(sql)
    results = cur.fetchall()
    print("Printing results", results)
    return jsonify(results)

@app.route('/price/<comparator>')
def get_price():
    pass