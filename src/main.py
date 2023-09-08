from flask import Flask, request


app = Flask(__name__)


@app.route('/bring_elevator', methods=['POST'])
def bring_elevator():
    """A person requests an elevator be sent to their current floor

    Request JSON payload
    {
        "floor": integer                        // Floor number where the car should pick person.
    }
    
    Response JSON payload
    {
        "command": "go_to_floor",
        "floor": integer                        // Floor number where the car should pick person.
    }
    """

    floor = get_floor_from_request()
    res = {
        "command": "bring_elevator",
        "floor": floor,
    }
    return res


@app.route('/go_to_floor', methods=['POST'])
def go_to_floor():
    """A person requests that they be brought to a floor

    Request JSON payload
    {
        "floor": integer                        // Floor number where the car should go with person.
    }
    
    Response JSON payload
    {
        "command": "go_to_floor",
        "floor": integer                        // Floor number where the car should go with person.
    }
    """

    floor = get_floor_from_request()
    res = {
        "command": "go_to_floor",
        "floor": floor,
    }
    return res


@app.route('/get_all_servicing_floors', methods=['GET'])
def get_servicing_floors():
    """An elevator car requests all floors that its current passengers are servicing (e.g. to light up the buttons that show which floors the car is going to)
    
    Request doesn't expect parameters.

    Response JSON payload
    {
        "command": "get_all_servicing_floors",
        "floor_list": list_of_integers          // List of integers containing the servicing floor numbers.
    }
    """

    res = {
        "command": "get_all_servicing_floors",
        "servicing_floors": [3, 6, 10],
    }
    return res


@app.route('/get_next_servicing_floor', methods=['GET'])
def get_next_servicing_floor():
    """An elevator car requests the next floor it needs to service
    
    Request doesn't expect parameters.
    
    Response JSON payload
    {
        "command": "get_next_servicing_floor",
        "floor": integer                        // Next servicing floor number integer value.
    }
    """

    res = {
        "command": "get_next_servicing_floor",
        "floor": 3,
    }
    return res


#  Helper methods

def throw_if_parameter_not_found(jsn, parameter_name: str):
    if parameter_name not in jsn:
        raise Exception(f'Invalid parameters: "{parameter_name}" not found')


def throw_if_parameter_was_none(parameter: object, parameter_name: str):
    if parameter is None:
        raise Exception(f'Invalid parameter value: "{parameter_name}" was None')


def throw_if_invalid_parameter_type(parameter: object, parameter_name: str, parameter_type: object):
    if not isinstance(parameter, parameter_type):
        raise Exception(f'Invalid parameter type: "{parameter_name}" was not {parameter_type}')


def get_floor_from_request():
    jsn = request.get_json()
    throw_if_parameter_not_found(jsn, 'floor')
    floor = jsn['floor']
    throw_if_parameter_was_none(floor, 'floor')
    throw_if_invalid_parameter_type(floor, 'floor', int)
    return floor


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
