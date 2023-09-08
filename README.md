This is a fully functional REST API endpoint prototype for the "Elevator" service. You can send requests and expect responses to test your REST API client code.
This prototype will NOT produce any side effects.


Starting the "Elevator" service
-------------------------------
1. Start a command line terminal window.

2. In the terminal window, change directory to your cloned folder "api_prototype".

3. Run the following script in the terminal window, optionally run the commands in that script individually:

```
install_and_start.cmd
```

Invoking the REST API with Curl
-------------------------------
To invoke the API with "curl" please use the following commands:

```
curl -d "{""floor"":3}" -H "Content-Type: application/json" -X POST http://localhost:8080/bring_elevator

curl -d "{""floor"":10}" -H "Content-Type: application/json" -X POST http://localhost:8080/go_to_floor

curl http://localhost:8080/get_all_servicing_floors

curl http://localhost:8080/get_next_servicing_floor
```


REST API documentation
----------------------

bring_elevator
--------------
**Purpose:**                A person requests that they be brought to a floor

**Method:**                 POST

**Endpoint:**               `http://localhost:8080/bring_elevator`

**Request JSON payload:**
```
    {
        "floor": integer                        // Floor number where the car should pick person.
    }
```

**Response JSON payload:**
```
    {
        "command": "go_to_floor",
        "floor": integer                        // Floor number where the car should pick person.
    }
```

go_to_floor
-----------
**Purpose:**                A person requests that they be brought to a floor

**Method:**                 POST

**Endpoint:**               `http://localhost:8080/go_to_floor`

**Request JSON payload:**
```
    {
        "floor": integer                        // Floor number where the car should go with person.
    }
```

**Response JSON payload:**
```
    {
        "command": "go_to_floor",
        "floor": integer                        // Floor number where the car should go with person.
    }
```

get_all_servicing_floors
------------------------
**Purpose:**                An elevator car requests all floors that its current passengers are servicing (e.g. to light up the buttons that show which floors the car is going to)

**Method:**                 GET

**Endpoint:**               `http://localhost:8080/get_all_servicing_floors`

**Request JSON payload:**   Request doesn't expect parameters.

**Response JSON payload:**
```
    {
        "command": "get_all_servicing_floors",
        "floor_list": list_of_integers          // List of integers containing the servicing floor numbers.
    }
```

get_next_servicing_floor
------------------------
**Purpose:**                An elevator car requests the next floor it needs to service

**Method:**                 GET

**Endpoint:**               `http://localhost:8080/get_next_servicing_floor`

**Request JSON payload:**   Request doesn't expect parameters.

**Response JSON payload:**
```
    {
        "command": "get_next_servicing_floor",
        "floor": integer                        // Next servicing floor number integer value.
    }
```