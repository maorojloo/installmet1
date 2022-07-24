from calendar import c
from statistics import mode
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import xmltodict
import json
from . import models, serializers


@api_view(['GET', 'POST'])
def sfapi(request, shenasepardakht):
    objj = None
    print("----------------------")
    try:
        objj = models.CallInstallment.objects.get(
            shenasepardakht=shenasepardakht)
    except Exception as e:
        print("----")
        print(e)
        print("----")

    if objj != None:
        serializer = serializers.CallInstallmentSerializer(objj)

        return Response({'json Response': serializer.data})

    url = "http://192.168.1.42/soap"
    # structured XML
    payload = f"""
    
            <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ins="http://www.iraninsurance.ir/installmentServices">
            <soapenv:Header/>
            <soapenv:Body>
                <ins:callInstallment>
                    <ins:loginRequest>
                        <ins:Username>hosaco</ins:Username>
                        <ins:Password>hosaco</ins:Password>
                    </ins:loginRequest>
                    <ins:request>
                        <ins:controlCode>{shenasepardakht}</ins:controlCode>
                    </ins:request>
                </ins:callInstallment>
            </soapenv:Body>
            </soapenv:Envelope>
            
            """
    # headers
    headers = {
        'Content-Type': 'text/xml; charset=utf-8'
    }
    # POST request
    response = requests.request("POST", url, headers=headers, data=payload)

    obj = xmltodict.parse(response.text)
    print("----------------------")
    print(obj)
    print("----------------------")
    obj = obj["soap:Envelope"]["soap:Body"]["callInstallmentResponse"]["controlCodes"]
    obj["installmentDate"] = obj["installmentDate"].replace("/", "")

    q = models.CallInstallment(amount=obj["amount"], controlCodeResult=obj["controlCodeResult"], installmentDate=obj["installmentDate"],
                               insuredName=obj["insuredName"], paymentStatus=obj["paymentStatus"], policyNo=obj["policyNo"], shenasepardakht=shenasepardakht)
    q.save()
    return Response({'json Response': obj})
