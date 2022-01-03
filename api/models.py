from django.db import models

class HotelWine(models.Model):
    보유와인번호 = models.AutoField(primary_key=True)
    와인이름 = models.CharField(max_length=100)
    재고 = models.IntegerField(default=0)

    class Meta:
        db_table = 'HotelWine'

class orderlist(models.Model):
    주문넘버 = models.AutoField(primary_key=True)
    와인이름 = models.CharField(default='', max_length=255, null=True)
    룸넘버 = models.IntegerField(default=0)
    주문시간 = models.DateTimeField(auto_now_add=True, blank=True)
    class Meta:
        db_table = 'orderlist'