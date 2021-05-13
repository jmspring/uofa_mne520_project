from flask import Flask, render_template
import pandas as pd
import pymssql
from decimal import Decimal

app = Flask(__name__)

# Load points within the bounds specified
def load_bounded_points(lower_left_lat, lower_left_lon, upper_right_lat, upper_right_lon):
    # MSSQL requires that Between queries require that the lower number
    # be the first, the larger the second
    latMin = min(lower_left_lat, upper_right_lat)
    latMax = max(lower_left_lat, upper_right_lat)
    lonMin = min(lower_left_lon, upper_right_lon)
    lonMax = max(lower_left_lon, upper_right_lon)

    columns = ['id', 'url', 'site_name', 'latitude', 'longitude']
    with pymssql.connect('db', 'SA', 'GoldIsTheBestMetal!', 'mrds') as conn:
        with conn.cursor() as cursor:
            sql = 'select dep_id as id, url, site_name, latitude, longitude from mrds where latitude between {} and {} and longitude between {} and {};'.format(latMin, latMax, lonMin, lonMax);
            cursor.execute(sql)
            row = cursor.fetchall()
            df = pd.DataFrame(row, columns = columns)
    return df

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/points/<lower_left_lat>/<lower_left_lon>/<upper_right_lat>/<upper_right_lon>')
def points(lower_left_lat, lower_left_lon, upper_right_lat, upper_right_lon):

    # convert string values to decimal
    lower_left_lat = Decimal(lower_left_lat.strip(' "'))
    lower_left_lon = Decimal(lower_left_lon.strip(' "'))
    upper_right_lat = Decimal(upper_right_lat.strip(' "'))
    upper_right_lon = Decimal(upper_right_lon.strip(' "'))
    
    # find points within the bounds
    points= load_bounded_points(lower_left_lat, lower_left_lon, upper_right_lat, upper_right_lon)
    return points.to_json()


