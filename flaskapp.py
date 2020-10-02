from flask import Flask, jsonify
import pandas as pd
import json
import gspread

app = Flask(__name__)


def get_data():

    # setup service account and add confic file --> https://gspread.readthedocs.io/en/latest/index.html
    gc = gspread.service_account()
    sh = gc.open("test_data")  # sheet name
    data = sh.sheet1.get_all_values()  # all rows and cols
    header, data = data[0], data[1:]  # header and data
    df = pd.DataFrame(
        data,
        columns=header
    )
    result = df.to_json(orient="records")
    parsed = json.loads(result)
    return parsed


@app.route('/')
def serve():
    try:
        res = get_data()
        return jsonify(get_data())
    except:
        return jsonify({"data": "none"})


if __name__ == '__main__':
    app.run(debug=True)
