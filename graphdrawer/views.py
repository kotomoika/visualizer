# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from pymongo import MongoClient
from django.shortcuts import render
from datetime import datetime

client = MongoClient("mongodb://admin:admin123@ds161121.mlab.com:61121/sensory_data")
db = client.sensory_data


def data_provider(request):
    data_list = {
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
        11: 0,
        12: 0,
        13: 0,
        14: 0,
        15: 0,
        16: 0,
        17: 0,
        18: 0,
        19: 0,
        20: 0,
        21: 0,
        22: 0,
        23: 0,
    }
    elements = []
    choosedDate = 0

    if request.method == "POST":
        choosedDate = request.POST.get("date", "")
        start = datetime.strptime(choosedDate + " 06:00", '%Y-%m-%d %H:%M').strftime('%m/%d/%Y %H:%M')
        end = datetime.strptime(choosedDate + " 23:59", '%Y-%m-%d %H:%M').strftime('%m/%d/%Y %H:%M')

        elements = db.data.find({
            "date_time": {
                '$gte': start,
                '$lt': end
            }
        })

        print(choosedDate)

    for e in elements:
        data_list[datetime.strptime(e["date_time"],'%m/%d/%Y %H:%M').hour] += 1

    res_list = []
    #for key, value in data_list:
    #    res_list.append(value)

    #data_list = sorted(data_list.keys(), key=lambda i: float(i[1]))
    for key in sorted(data_list.iterkeys()):
        res_list.append(data_list.get(key))
    return render(request, 'index.html', {'result': res_list, "choosedDate":choosedDate},)