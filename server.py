from flask import Flask, render_template
from models import Orders, db
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
# app.config.from_object('config')

db_credentials = {
    'user': 'score',
    'passwd': 'Rysherat2',
    'host': 'shopscore.devman.org',
    'db_name': 'shop'
}

# app.config['SQLALCHEMY_DATABASE_URI']
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']

db.init_app(app)

@app.route('/')
def score():
    orders = Orders.query.first()
    print(orders)
    return render_template('score.html')

if __name__ == "__main__":
    app.run()
