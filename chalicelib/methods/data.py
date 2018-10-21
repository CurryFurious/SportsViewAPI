from chalicelib.methods.utils import get_dynamo_table
from chalicelib.models.data import DataModel
import arrow

table = get_dynamo_table('Data')

def get_all_data():
    data = table.scan()['Items']
    return sorted(data, key=lambda x: arrow.get(x['time']).datetime)

def post_data(data):
    table.put_item(
        Item=DataModel().dump(data).data
    )


def post_all_data(data):
    with table.batch_writer() as batch:
        for d in data:
            batch.put_item(
                Item=DataModel().dump(d).data
            )
