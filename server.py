from flask_app import app                                               # Import flask app
from flask_app.controllers import root_controller                       # Import Controller

if __name__=="__main__":   
    app.run(debug=True)    