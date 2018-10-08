from datetime import timedelta


def get_score_color(score_minutes):
    green_time = 7
    yellow_time = 30
    if score_minutes <= timedelta(minutes=green_time):
        return '#00FF7F'
    elif score_minutes <= timedelta(minutes=yellow_time):
        return '#FFFF00'
    else:
        return '#FF0000'

