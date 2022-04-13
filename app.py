# import necessary libraries
# from models import create_classes
import pandas as pd
import os
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlite3 import connect 
import json

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect,
    jsonify)


#####################################################################
engine = create_engine("sqlite:///data/mydatabase.db")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
print(Base.classes.keys())

Healthatlas = Base.classes.healthatlas
#Actors = Base.classes.actors

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
# ---------------------------------------------------------
# Web site
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data.html")
def data():

    return render_template("data.html")

@app.route("/templates/map.html")
def map():

    return render_template("map.html")

@app.route("/templates/d3_chart.html")
def d3_chart():
    return render_template("d3_chart.html")




# ---------------------------------------------------------

# API to call "when data.html" page is loading with community information table
@app.route("/api/community")
def community_grid():
    session = Session(engine)
    
    results = [list(r) for r in results]

    table_results = {
        "table": results
    }
    
    
    session.close()
    
    return jsonify(table_results)


@app.route("/api/geojson")
def map_data():
    with open('data/geo.json', 'r') as file:
        your_data = json.loads(file.read())
    # print(your_data)
    return jsonify(your_data)

@app.route('/api/d3_chart/<field_x>/<field_y>')
def d3_chart_api(field_x, field_y):
    session = Session(engine)
    x_column = getattr(Healthatlas, field_x)
    y_column = getattr(Healthatlas, field_y)
    results = session.query(x_column, y_column).all()
    results = [list(r) for r in results]
    session.close()
    return jsonify(results)




if __name__ == "__main__":
    app.run()