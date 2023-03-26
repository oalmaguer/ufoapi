from flask import *
import json, time
import csv
import pandas as pd



app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/', methods=['GET'])
def home():
    data_set = {'Page': 'Home', 'Message': 'Welcome to the UFO Sightings API', 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump

@app.route('/test', methods=['GET'])
def home():
    data_set = {'Page': 'Home', 'Message': 'Welcome to the UFO Sightings API', 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump

@app.route('/api/city/<string:city>', methods=['GET'])
def request_city(city):
    page =  city.split("=")[1];
    city_formatted =  city.split("&")[0];
    print(city_formatted)
    cols = ["state", "country", "shape", "city", "report_link", "text", "stats"]
    print("hi2");

    df = pd.read_csv("ufo.csv", usecols=cols)
    city =  city.lower().replace(' ', '')

    df['city'].str.lower()
    df['city'].str.strip()
    filtered_data = df[df['city'].str.lower().str.replace(' ', '') == city_formatted]
    # Define the number of results per page
    results_per_page = 150
    # Calculate the start and end indices for the current page
    start_index = (int(page)) * results_per_page
    end_index = start_index + results_per_page

    print(start_index, end_index)
    # Get the results for the current page
    page_data = filtered_data.iloc[start_index:end_index].to_dict(orient='records')

    # Create a dictionary with the results for the current page
    result = {
        "page": page,
        "per_page": results_per_page,
        "total_results": len(df),
        "total_pages": len(df) // results_per_page + 1,
        "data": page_data
    }

    # Return the results in JSON format
    return jsonify(result)

@app.route('/api/state/<string:state>', methods=['GET'])
def request_state(state):
    page =  state.split("=")[1];
    state_formatted =  state.split("&")[0];
    
    cols = ["state", "country", "shape", "city", "report_link", "text", "stats"]

    df = pd.read_csv("ufo.csv", usecols=cols)
    state =  state.lower().replace(' ', '')

    filtered_data = df[df['state'].str.lower() == state_formatted]

    # Define the number of results per page
    results_per_page = 150
    # Calculate the start and end indices for the current page
    start_index = (int(page)) * results_per_page
    end_index = start_index + results_per_page

    print(start_index, end_index)
    # Get the results for the current page
    page_data = filtered_data.iloc[start_index:end_index].to_dict(orient='records')

    # Create a dictionary with the results for the current page
    result = {
        "page": page,
        "per_page": results_per_page,
        "total_results": len(df),
        "total_pages": len(df) // results_per_page + 1,
        "data": page_data
    }

    # Return the results in JSON format
    return jsonify(result)

@app.route('/api/country/<string:country>', methods=['GET'])
def request_country(country):
    page =  country.split("=")[1];
    country_formatted =  country.split("&")[0];
    print("Page: ", page);
    
    cols = ["state", "country", "shape", "city", "report_link", "text", "stats"]


    df = pd.read_csv("ufo.csv", usecols=cols)
    print(df['country'].str.lower())
    country =  country.lower().replace(' ', '')
    print(country_formatted)

    filtered_data = df[df['country'].str.lower() == country_formatted]

    # Define the number of results per page
    results_per_page = 150
    # Calculate the start and end indices for the current page
    start_index = (int(page)) * results_per_page
    end_index = start_index + results_per_page

    print(start_index, end_index)
    # Get the results for the current page
    page_data = filtered_data.iloc[start_index:end_index].to_dict(orient='records')

    # Create a dictionary with the results for the current page
    result = {
        "page": page,
        "per_page": results_per_page,
        "total_results": len(df),
        "total_pages": len(df) // results_per_page + 1,
        "data": page_data
    }

    # Return the results in JSON format
    return jsonify(result)


if __name__ == '__main__':
    app.run(port=8080)