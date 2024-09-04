from flask import Flask, render_template
from flask import request
import data_process

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template("anli.html")


@app.route('/temperature', methods=["get", "post"])
def temperature():  # put application's code here
    city = request.values.get("city")
    return data_process.temperature_singele(city)


@app.route("/map")
def map():
    return render_template("SecondScreen.html")

@app.route("/main")
def main():
    return render_template("map1.html")

if __name__ == '__main__':
    app.run()


@app.route('/ajax', methods=["get", "post"])  # 默认值是get所以只能接收get请求，只需要在后面加上post就可以接收post请求了
def firstmap():  # put application's code here
    name = request.values.get("name")
    # score = request.values.get("value")
    return '1000'
