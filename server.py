from flask import Flask, render_template
from models import Orders, db
from config import Config
from datetime import datetime, timedelta
from score_process import get_score_color

app = Flask(__name__)
app.config.from_object(Config)


db.init_app(app)


@app.route('/')
def score():
    today_orders = Orders.query.filter(Orders.created >= datetime.today().date())
    count_today_orders = today_orders.count()
    unconfirmed_orders = today_orders.filter(Orders.confirmed.is_(None))
    count_unconfirmed_orders = unconfirmed_orders.count()
    if count_unconfirmed_orders > 0:
        max_wait_time_orders = unconfirmed_orders.order_by(datetime.today() - Orders.created).first()
        max_wait_time = datetime.today() - max_wait_time_orders.created
    else:
        max_wait_time = timedelta(minutes=0)
    score_color = get_score_color(max_wait_time)
    printed_max_wait_time = max_wait_time - timedelta(microseconds=max_wait_time.microseconds)
    return render_template('score_screen.html',
                           score_minutes=printed_max_wait_time,
                           count_unconfirmed_orders=count_unconfirmed_orders,
                           count_today_orders=count_today_orders,
                           score_color=score_color)


if __name__ == "__main__":
    app.run()
