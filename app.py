from chalice import Chalice
from chalicelib.methods.get_players import get_all_players, get_player
from chalicelib.methods.data import post_data, get_all_data, post_all_data
from chalicelib.methods.stats import get_all_stats, get_stats_num, get_condensed_stats
import boto3

app = Chalice(app_name='SportsViewAPI')


@app.route('/players/all', cors=True)
def get_players():
    return get_all_players()


@app.route('/data/all', cors=True, methods=['GET', 'POST'])
def get_data():
    request = app.current_request
    if request.method == 'GET':
        return get_all_data()
    elif request.method == 'POST':
        return post_all_data(request.json_body)


@app.route('/data', cors=True, methods=['POST'])
def post_singular_data():
    request = app.current_request
    if request.method == "POST":
        return post_data(request.json_body)


@app.route('/stats', cors=True)
def get_stats():
    return get_all_stats()


@app.route('/stats/num', cors=True)
def get_num():
    return get_stats_num()


@app.route('/stats/lite', cors=True)
def get_condensed():
    return get_condensed_stats()
