from rest_framework import viewsets
from .serializers import CornerImageSerializer
from ..models import CornerImage
from ..models import PriceTable, LocationTable
from django.http import JsonResponse
import json

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from geopy.distance import geodesic
# tibero DB 관련 import
import pyodbc


def calculate_distance(coord1, coord2):
    # coord1과 coord2는 각각 (위도, 경도) 형태의 튜플이어야 합니다.
    distance = geodesic(coord1, coord2).meters
    return distance


class CornerImageViewSet(viewsets.ModelViewSet):
    queryset = CornerImage.objects.all().order_by('-uploaded')
    serializer_class = CornerImageSerializer



@method_decorator(csrf_exempt, name='dispatch')
def get_info_view(request):
    if request.method == 'POST':
        # 위에서 찍은 사진이 어떤 제품 사진인지 self.product_name에 있으므로 추가 정보 가져오기
        try:
            data = json.loads(request.body)
            product_name = data.get('product_name')

            product = PriceTable.objects.get(name=product_name)    ## 프론트에서 보낸 data는 product_name
            price = product.price
            info = product.info

            response_data = {'product_name': product_name, 'price': float(price), 'info':info}
            return JsonResponse(response_data)
        except PriceTable.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
@method_decorator(csrf_exempt, name='dispatch')
def get_info_by_barcode(request):
    if request.method == 'POST':
        # 위에서 찍은 사진이 어떤 제품 사진인지 self.product_name에 있으므로 추가 정보 가져오기
        try:
            data = json.loads(request.body)
            barcode_num = data.get('barcode_num')

            product = PriceTable.objects.get(barcode_num=barcode_num)    ## 프론트에서 보낸 data는 product_name
            name = product.name
            price = product.price
            info = product.info

            response_data = {'product_name': name, 'price': float(price), 'info':info}
            return JsonResponse(response_data)
        except PriceTable.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


@method_decorator(csrf_exempt, name='dispatch')
def get_info_by_qr(request):
    if request.method == 'POST':
        # 위에서 찍은 사진이 어떤 제품 사진인지 self.product_name에 있으므로 추가 정보 가져오기
        try:
            data = json.loads(request.body)
            qr = data.get('qr')

            product = PriceTable.objects.get(qr_url=qr)    ## 프론트에서 보낸 data는 product_name
            name = product.name
            price = product.price
            info = product.info

            response_data = {'product_name': name, 'price': float(price), 'info':info}
            return JsonResponse(response_data)
        except PriceTable.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


@method_decorator(csrf_exempt, name='dispatch')
def get_location_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            lati = float(data.get('latitude'))
            longi = float(data.get('longitude'))
            nowPos = (lati, longi)
            print(nowPos)

            stores = LocationTable.objects.all()
            storeList = []
            for store in stores:
                slat = float(store.latitude)
                slong = float(store.longitude)
                storePos = (slat, slong)
                tempDist = int(calculate_distance(nowPos, storePos))
                storeList.append([store.name, tempDist, store.address])
            storeList.sort(key=lambda x:x[1])
            for elem in storeList:
                print(elem)
            serialized_list = json.dumps(storeList)
            return JsonResponse({'store_list': serialized_list})
        except LocationTable.DoesNotExist:
            return JsonResponse({'error': 'DB not found'}, status=404)
        except Exception as e:
            print(e)
            return JsonResponse({'error': str(e)}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
def test_function(request):
    # if request.method == 'GET':
    # 예시: 서울과 뉴욕 간의 거리 계산
    seoul_coords = (37.5665, 126.9780)  # 서울 위도, 경도
    new_york_coords = (40.7128, -74.0060)  # 뉴욕 위도, 경도
    print('################################')
    lati = float('37.3228642')
    longi = float('127.1273101')
    nowPos = (lati, longi)

    stores = LocationTable.objects.all()
    storeList = []
    for store in stores:
        slat = float(store.latitude)
        slong = float(store.longitude)
        storePos = (slat, slong)
        tempDist = int(calculate_distance(nowPos, storePos))
        storeList.append([store.name, tempDist, store.address])
    storeList.sort(key=lambda x:x[1])
    print(storeList)
    print('################################')

    distance_meters = calculate_distance(seoul_coords, new_york_coords)
    print(f"The distance between Seoul and New York is {distance_meters:.2f} meters.")
    return distance_meters




def get_data_from_database(request):
    db = pyodbc.connect("DSN=tmax;UID=sys;PWD=tibero")
    cursor = db.cursor()
    cursor.execute("select * from test_table")

    for row in cursor:
        for elem in row:
            print(elem, end='')
        print()
    
    db.close()