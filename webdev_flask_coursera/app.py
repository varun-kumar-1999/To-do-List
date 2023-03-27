from flask import Flask  #,render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
#Secret key for csrf token
app.config['SECRET_KEY'] = 'sbvc-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy (app)
'''@app.route('/')
#@app.route('/i')
def index():
    return render_template('i.html')

@app.route('/abt.html')
def about():
    return render_template('/abt.html')'''
from routes import *



if __name__ == '__main__':
    app.run(debug = True)

