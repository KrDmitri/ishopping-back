from django.db import models
import time, random
import requests
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser

# Create your models here.
class CornerImage(models.Model):
    picture = models.ImageField()
    picture_id = models.CharField(max_length=20, blank=True)
    info = models.CharField(max_length=200, blank=True)
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Corner Image took at {}".format(self.uploaded.strftime('%Y-%m-%d %H:%M'))
    
    def save(self, *args, **kargs):
        # picture_id 설정
        # new_id = str(round(time.time()))
        # new_id += str(int(round(random.random(), 3) * 1000))
        # self.picture_id = new_id

        # ai 서버로 사진 전송
        image_data = self.picture.read()

        target_server_url = "http://ec2-43-201-111-213.ap-northeast-2.compute.amazonaws.com:8080/api-corner-ai/corner_ai/"

        files = {'picture': (self.picture.name, image_data)}
        data = {'picture_id': self.picture_id}
        response = requests.post(target_server_url, files=files, data=data)

        if response.status_code == 201:
            print("image transfer success")
        else:
            print("failed to send image")

        # ai 서버에서 정보 data GET으로 가져오기
        try:
            response = requests.get(target_server_url)
            data = response.json()
            for elem in data:
                if elem["picture_id"] == self.picture_id:
                    print(elem)
                    self.info = elem["info"]
        except requests.RequestException as e:
            print("error: ", str(e))

        super().save(*args, **kargs)