from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .models import Approvals
from .serializers import ApprovalsSerializers
import pickle
import joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd

class ApprovalsView(viewsets.ModelViewSet):
    queryset = Approvals.objects.all()
    serializer_class = ApprovalsSerializers

@api_view
def apprevereject(request):
    try:
        mdl = joblib.load("C:/Users/ojare/AIML/Bank-Loan-Authentication/loan_model.pkl")
        mydata = request.data
        unit = np.array(list(mydata.values()))
        unit = unit.reshape(1,-1)
        scalers = joblib.load()
        X = scalers.transform(unit)
        y_pred = mdl.predict(X)
        y_pred = (y_pred>0.58)
        newdf = pd.DataFrame(y_pred, columns=["Status"])
        newdf = newdf.replace({True: "Approved", False: "Rejected"})
        return JsonResponse("Your Status is {}".format(newdf), safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)