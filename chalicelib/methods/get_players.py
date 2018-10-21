from chalicelib.methods.utils import get_dynamo_table

table = get_dynamo_table('players')

def get_all_players():
    return table.scan()['Items']

def get_player(player_name):
    return table.get_item(
        Key={
            'player': player_name
        }
    )['Item']
