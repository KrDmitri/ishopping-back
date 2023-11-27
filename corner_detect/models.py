from django.db import models
import time, random
import requests
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser

# Create your models here.
class TestTable(models.Model):
    name = models.CharField(max_length=255)

class PriceTable(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)


class CornerImage(models.Model):
    picture = models.ImageField()
    picture_id = models.CharField(max_length=14, blank=True)
    info = models.CharField(max_length=200, blank=True)
    product_name = models.CharField(max_length=200, blank=True, default='')
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Corner Image took at {}".format(self.uploaded.strftime('%Y-%m-%d %H:%M'))
    
    def save(self, *args, **kargs):
        ##### ai 서버로 사진 전송 #####
        image_data = self.picture.read()

        target_server_url = "ec2-43-201-249-72.ap-northeast-2.compute.amazonaws.com:8080/api-corner-ai/process-image/"

        files = {'picture': (self.picture.name, image_data)}
        data = {'picture_id': self.picture_id}
        response = requests.post(target_server_url, files=files, data=data)

        if response.status_code == 200 or response.status_code == 201:
            print("image transfer success")
        else:
            print("failed to send image")
        
        data = response.json()
        self.product_name = data["product_name"]
        print(data)

        # # 위에서 찍은 사진이 어떤 제품 사진인지 self.product_name에 있으므로 추가 정보 가져오기
        try:
            price_model = PriceTable.objects.get(name=self.product_name)
            price = price_model.price
        except:
            price = "가격 정보 없음"


        self.info = "이 제품은 " + self.product_name + "입니다. 가격은 " +  price + "입니다."

        super().save(*args, **kargs)