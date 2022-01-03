from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view
from django.http import HttpResponse, QueryDict

@api_view(['POST'])
def orderWine(request):
    if request.method != 'POST':
        return HttpResponse("Bad Request", status=400)

    requestBody = QueryDict.dict(request.data)
    wineName = requestBody['wineName']
    roomNum = requestBody['roomNum']
    print(wineName)
    print(roomNum)
    # 주문 승인 -> 'order' 테이블에서 삭제
    return HttpResponse("success")


