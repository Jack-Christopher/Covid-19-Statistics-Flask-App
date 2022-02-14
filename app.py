import os 
import sys
import requests
from datetime import datetime
from flask import Flask, render_template, request, send_from_directory , redirect, session, url_for


def get_countries():
    url = "https://covid-193.p.rapidapi.com/countries"

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "46329f91e4msh8baa5b2a7080630p101ab2jsncc33c8e9656b"
        }

    response = requests.request("GET", url, headers=headers)
    response = response.text
    countries = dict(eval(response))
    countries = countries['response']

    return countries


def get_statistics(country="Peru"):
    url = "https://covid-193.p.rapidapi.com/statistics"

    querystring = {"country":country}

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "46329f91e4msh8baa5b2a7080630p101ab2jsncc33c8e9656b"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.json()
    statistics = dict(response)
    statistics = statistics['response'][0]

    for key, value in statistics.items():
        if type(value) == dict:
            for key2, value2 in value.items():
                if value2 == None:
                    value[key2] = 'Unknown'
    
    return statistics


app = Flask(__name__)
app.secret_key = 'very-secret-key'

@app.route('/')
def index():
    countries = get_countries()
    return render_template("index.html", countries=countries)

@app.route('/statistics/<country>')
def statistics(country):
    statistics = get_statistics(country)
    return render_template("statistics.html", statistics=statistics)


@app.route('/<page>')
def web_dir(page):
	return render_template("/" + page)

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), '/img/icon.jpg')


if __name__ == '__main__':
   app.run(debug = True)
