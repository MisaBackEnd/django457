from django.shortcuts import render
from django.http import HttpResponse 
from django.http import JsonResponse
import requests

def index(request):
    # url = "https://e-volution.co/django7633-test4a4"
    # headers = {
    #    'Authorization': 'Basic dXNlcjQ1OjU2ZmVkMjM1ZGY0NTNmYmM4MjZkZGMyM2QzZmRiY2FzNzNjNGZz'
    # }
    # res = requests.get(url, headers=headers, verify=False)
    data = {
        "frameworks": {
            "Bottle": "28 %",
            "Web2Py": "55 %",
            "Flask": "35 %",
            "Django": "65 %",
            "CherryPy": "16 %"
        },
        "desc": [
            "Web2Py: Create, modify, deploy and manage application from anywhere using your browser",
            "Bottle: Is a fast, simple and lightweight WSGI micro web-framework for Python",
            "Django: Is a high-level Python web framework that encourages rapid development and clean",
            "CherryPy: Is a pythonic, object-oriented web framework",
            "Flask: provides configuration and conventions, with sensible defaults, to get started"
        ]
    }
    frameworks = data["frameworks"]
    desc = { d.split(":")[0]:d.split(":")[1] for d in data["desc"]}
    order_data = {}
    for k,v in frameworks.items():
        val = v.replace(" %", "")
        val = int(val)
        order_data[val] = k
    print(order_data)
    order_final = list(order_data.keys())
    order_final.sort()
    print(order_final)
    frameworks = { order_data[k]:{"usage":"{} %".format(k), "desc":desc[order_data[k]]} for i,k in enumerate(order_final)}
    # return HttpResponse(res.status_code)
    return JsonResponse(frameworks)
