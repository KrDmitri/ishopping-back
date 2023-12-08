from rest_framework import viewsets
from .serializers import CornerImageSerializer
from ..models import CornerImage
from ..models import PriceTable
from django.http import JsonResponse
import json

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# tibero DB 관련 import
import pyodbc


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

            response_data = {'product_name': product_name, 'price': float(price)}
            return JsonResponse(response_data)
        except PriceTable.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

def get_data_from_database(request):
    db = pyodbc.connect("DSN=tmax;UID=sys;PWD=tibero")
    cursor = db.cursor()
    cursor.execute("select * from test_table")

    for row in cursor:
        for elem in row:
            print(elem, end='')
        print()