from flask_app import app                                               # App is used to handle routes
from flask import render_template, session, redirect, request, jsonify

# ////////////////////////////////////////////////////////
# ROOT CONTROLLER
# ////////////////////////////////////////////////////////

# //// SHOW /////////////////////////////////////

@app.route('/')                                                         # Main Page
def root():
    print("******** in index *******************")
    return render_template("index.html")

# //// UTILITIES /////////////////////////////////


# //// CREATE ////////////////////////////////////


# //// RETRIEVE ////////////////////////////////////


# //// UPDATE ////////////////////////////////////


# //// DELETE ////////////////////////////////////


# //// 404 CATCH //////////////////////////////////

# **** Ensure that if the user types in any route other than the ones specified, 
#           they receive an error message saying "Sorry! No response. Try again ****
@app.errorhandler(404) 
def invalid_route(e): 
    return "Sorry! No response. Try again."