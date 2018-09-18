from flask import Flask, render_template
from models import Orders, db
from config import Config
from datetime import datetime, timedelta, time

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
    # orders = Orders.query.first()
    today_orders = Orders.query.filter(Orders.created >= datetime.today().date())
    print(today_orders.count())
    unconfirmed_orders = today_orders.filter(Orders.confirmed==None)
    print('UCONFIRMED ORDERS: {}'.format(unconfirmed_orders.count()))
    print(unconfirmed_orders)
    if unconfirmed_orders.count() > 0:
        confirmed_orders = today_orders.count() - unconfirmed_orders.count()
        print('CONFIRMED ORDERS: {}'.format(confirmed_orders))
    # score = (datetime.today() - today_orders)
        delta_order = unconfirmed_orders.order_by(datetime.today() - Orders.created).first()
        timedelta_score = (datetime.today() - delta_order.created)
        print(timedelta_score)
        score_minutes = timedelta_score.seconds/60
        print(score_minutes)
        print('{}:{}'.format(timedelta_score.seconds//60, timedelta_score.seconds%60))
    else:
        score_minutes = 0
    # Here will be a call of color function
    return render_template('score.html')


if __name__ == "__main__":
    app.run()
