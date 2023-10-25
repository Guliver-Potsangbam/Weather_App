from flask import Flask, render_template, request
import requests
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.htm")

@app.route("/result", methods=['POST', 'GET'])
def get_weather_data():
    my_api_key = '743247021b9517d7e742224e0943946d'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    param = {
        'q': request.form.get('city'),
        'appid': my_api_key,
        'units': 'metric'
    }
    response = requests.get(url, params=param)
    data = response.json()
    return f"""<h1>Result:</h1>
    <p> Co-ordinates: {data['coord']}</p>
    <p> Temperature: {data['main']}</p>
    <p> All: {data}</p>
    """

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5002)
