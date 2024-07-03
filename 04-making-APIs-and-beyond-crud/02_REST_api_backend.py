# start this server with the command: fastapi dev 02_REST_api_backend.py
from fastapi import FastAPI, HTTPException, Body

app = FastAPI()

# This setup code is to mock out some data for our API to serve
users = {
    1: {
        'name': 'Tyler',
        'age': 72
    },
    2: {
        'name': 'Molly',
        'age': 66
    },
    3: {
        'name': 'Hades',
        'age': 4
    }
}

# The FastAPI uses these "decorators" a lot. Decorator allow you to write
# code that happens before and/or after the function the decorator applies to.
# In this first case it does a few things:
#   * Registers the URL "/" with the app, and associates this function with GET requests to that URL
#   * Takes our returned dictionary, turns it into JSON, puts that in an HTTP response, and sends it.
@app.get("/")
def read_root():
    return {"Hello": "World"}


# This route registers another URL for our server, /users/{anything}
# FastAPI decorator extracts anything in curly's from the URL, and assigns its
# value to a parameter with the same name. In this route you can see we search
# for a matching user id and either return it or send a 404 "not found" error.
@app.get("/users/{user_id}")
def read_user(user_id: int):
    if user_id in users:
        return users[user_id]
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    

# This time the decorator accepts a status code, which overrides the default (200) for a success
# Allowing us to simply return the new data we created for the user
@app.post("/users/{user_id}", status_code=201)
def create_user(user_id: int, name: str = Body(), age: int = Body()):
    if user_id in users:
        raise HTTPException(status_code=409, detail="User with that ID already exists")

    # add it to our list
    users[user_id] = {
        'name': name,
        'age': age
    }

    return users[user_id]


# Mini Exercise: Add another route to this API Server that
# follows the REST standard for items but for the PUT method
# So specifically your route needs to
#  * Accept the same body parameters as the above POST route
#  * Use the same route, but with the PUT method.
#  * Replace the specified user with the data supplied by the user, and return that user.
#  * Or raise an HTTPException if the specified user_id does not already exist.





