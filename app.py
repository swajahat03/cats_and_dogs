from flask import Flask, render_template,url_for
from flask_sqlalchemy import SQLAlchemy 
import logging
from datetime import datetime
import json
from flask import request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class animal (db.Model):
     id = db.Column(db.Integer, primary_key = True)
     time_clicked = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/', methods=['POST', 'GET'])
def index():
    print("ran_index")
    print(sorted(request.headers.keys()))
    with open("logs2.csv", "a") as csvfile:
        csvWriter = csv.writer(csvfile)
        headerData = []
        headerData.append(datetime.now())
        for key in sorted(request.headers.keys()):
            headerData.append(request.headers[key])
        csvWriter.writerow(headerData)
    return render_template('index.html')

@app.route('/img/kitten1.JPG', methods=['POST', 'GET'])
def kitten1():
    return render_template('cat.html')

@app.route('/img/kitten2.JPG', methods=['POST', 'GET'])
def kitten2():
    return render_template('cat.html')

@app.route('/img/kitten3.JPG', methods=['POST', 'GET'])
def kitten3():
    return render_template('cat.html')

@app.route('/img/puppy1.JPG', methods=['POST', 'GET'])
def puppy1():
    return render_template('dog.html')

@app.route('/img/puppy2.jpeg', methods=['POST', 'GET'])
def puppy2():
    return render_template('dog.html')

@app.route('/img/puppy3.jpg', methods=['POST', 'GET'])
def puppy3():
    return render_template('dog.html')



def __repr__(self):
    return '<Animal %r>' %self.id
    
if __name__ == "__main__":
    logging.basicConfig(filename='error.log', level=logging.DEBUG)
    app.run(debug=True, host="0.0.0.0", port=80) 
    



