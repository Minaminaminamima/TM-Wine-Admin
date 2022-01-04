from datetime import datetime, date
from django.shortcuts import render

from rest_framework.decorators import api_view
from django.http import HttpResponse, QueryDict
import pymysql.cursors

from .models import HotelWine
from .models import orderlist

#@api_view(['POST'])
def order(request):
    if request.method == 'POST' :
        wineName = request.POST.get('wineName', False)
        roomNum = request.POST.get('roomNum', False)

        # 수정필요
        conn = pymysql.connect(host='localhost',
                               user='mina',
                               password='1234',
                               db='adminDB')
        curs = conn.cursor()

        sql = "insert into orderlist(와인이름,룸넘버,주문시간) values(%s ,%s, %s);"
        curs.execute(sql, (wineName, roomNum, datetime.today().strftime('%Y-%m-%d %H:%M')))
        conn.commit()

        HttpResponse("okay") # for debugging


    orderlists = orderlist.objects.all()
    context = {'orderlists' :orderlists }
    return render(request, 'api/order.html', context)


def btn_click(request, order_num) :

    # 수정필요
    conn = pymysql.connect(host='localhost',
                           user='mina',
                           password='1234',
                           db='adminDB')
    curs = conn.cursor()

    # 삭제 선택된 row의 와인이름 검색
    sql = "SELECT 와인이름 FROM orderlist where 주문넘버= %s"
    curs.execute(sql, order_num)
    wine_name = curs.fetchone()

    # 재고 리스트 수정
    # 단 재고가 0 미만 되는 예외처리 하지않음
    sql = "UPDATE HotelWine  SET 재고 = 재고-1 WHERE 와인이름 = %s"
    curs.execute(sql, wine_name)

    # 주문목록에서 삭제
    # 주문번호 업데이트 되지않음 (1번이 삭제되어도 2번이 1번이 되지 않음)
    sql = "DELETE FROM orderlist where 주문넘버= %s"
    curs.execute(sql, order_num)
    conn.commit()

    orderlists = orderlist.objects.all()
    context = {'orderlists' :orderlists }

    return render(request, 'api/order.html', context)




def storage(request):
    hotelwines = HotelWine.objects.all()
    context = {'hotelwines' :hotelwines }

    return render(request, 'api/storage.html', context)




