from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import gspread
import json
import pandas as pd


def get_data():
    gc = gspread.service_account()
    sh = gc.open("test_data")
    data = sh.sheet1.get_all_values()
    header, data = data[0], data[1:]
    df = pd.DataFrame(
        data,
        columns=header
    )
    result = df.to_json(orient="records")
    parsed = json.loads(result)
    return parsed


@ api_view()
def test(request):
    try:
        res = get_data()
        return Response(get_data())
    except:
        return Response({"data": "none"})
