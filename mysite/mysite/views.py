from django.http import HttpResponse
from django.shortcuts import render
from .models import Condition
from .models import conditions
import pickle
import numpy as np
import os
from .settings import BASE_DIR

def index(request):
    form = []
    for con in conditions:
        form.append(Condition(con))
    context = {'form':form}
    print(form)
    return render(request, "index.html", context)


def submit_form(request):
    print("received")
    print(request.body)
    dict = {}
    for con in conditions:
        value = request.POST.get(con, '')
        dict[con] = value
    ret = get_result_from_model(dict)
    context = {'result': "have" if ret == 1 else "don't have"}
    return render(request, "result.html", context)


def get_result_from_model(inputData):
    filename = os.path.join(BASE_DIR, 'MLModel')
    print("name", filename)
    loaded_model = pickle.load(open(filename, "rb"))  # Press ⌘F8 to toggle the breakpoint.
    x = np.array([v for k, v in inputData.items()]).reshape(1, -1)
    result = loaded_model.predict(x)
    return result[0]