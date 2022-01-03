from django.db import models

class HotelWine(models.Model):
    보유와인번호 = models.AutoField(primary_key=True)
    와인번호 = models.IntegerField(default=0)
    군집 = models.IntegerField(default=0)
    평점 = models.DecimalField(max_digits=6, decimal_places=3)

    class Meta:
        db_table = 'HotelWine'

class Order(models.Model):
    주문 = models.AutoField(primary_key=True)
    보유와인번호 = models.ForeignKey(
        HotelWine,
        on_delete=models.CASCADE,
        db_column="보유와인번호",
    )
    룸넘버 = models.IntegerField(default=0)

    class Meta:
        db_table = 'Order'