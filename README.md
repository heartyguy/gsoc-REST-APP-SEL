# REST-API-Using-Flask

## Installation Instructions

Create a directory to hold the project

    mkdir tian-rest-flask-sel
    cd tian-rest-flask-sel

Clone the directory 

    git clone https://github.com/heartyguy/REST-API-Using-Flask-

# Go to the directory 

    cd tian-rest-flask-sel
  
# Create virtual environment

    virtualenv venv

# Activate virtual environment

    . venv/bin/activate
  
# Install the required dependencies

    pip install Flask
    pip install Flask-sqlalchemy
    pip install flask-triangle 
    

Deploy the app

    python ./app.py
   
    http://localhost:5000/ will display a table of all members using Angular
   


# Sample requests

check out the various requests in test.sh

    ./test.sh 

##Requests

While the server is deployed, GET, PUT and POST requests can be serviced

####GET

    curl -X GET http://localhost:5000/members

Returns a JSON that contains all members' name and phone number.

    curl -X GET http://localhost:5000/members/name

Returns a JSON that contains that member's name and phone number.

If the name is not found in the database, this will return a JSON indicating that no member is found.

####POST and PUT

POST and PUT requests are treated the same here. If name and phone are valid and there is no duplicate in the database, the new member is added. If name or phone is available, an json indicating input error is returned. If there is duplicate name in the database, the new member is not added and the error will reflect that.

curl -X POST -H "Content-Type: application/json" -d '{"name":"Matt", "phone":"4167483434"}' http://localhost:5000/members/add

curl -X PUT -H "Content-Type: application/json" -d '{"name":"David", "phone":"5197483434"}' http://localhost:5000/members/add








