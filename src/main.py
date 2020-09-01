from flask import Flask, request, abort
from marshmallow import Schema, fields

app = Flask(__name__)
app.config['DEBUG'] = True


class GraphNodeDTO(Schema):
    id = fields.Int(required=True)
    connections = fields.List(fields.Int(), required=True)


class SolveDTO(Schema):
    selected_node = fields.Int(required=True)
    graph = fields.List(fields.Nested(GraphNodeDTO), required=True)


@app.route('/', methods=['POST'])
def solve():
    errors = SolveDTO().validate(request.json)
    if errors:
        abort(400)

    mock_response = {
        "graph": [
            {
                "id": 1,
                "connections": [2, 3],
                "isBomb": False,
                "value": 4,
            }
        ]
    }
    return mock_response


if __name__ == '__main__':
    app.run()
