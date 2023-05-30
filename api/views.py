from rest_framework.decorators import api_view
from .service import Service
from rest_framework.response import Response


# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def method_wish(request):
    if request.method == 'GET':
        return Response(Service.get_all_wish())
    elif request.method == 'POST':
        return Response(Service.add_wish(request))
    else:
        return Response(Service.delete_wish(request))


@api_view(['POST', 'GET', 'DELETE'])
def method_confirm(request):
    if request.method == 'GET':
        return Response(Service.get_all_confirm())
    elif request.method == 'POST':
        return Response(Service.add_confirm(request))
    elif request.method == 'DELETE':
        return Response(Service.delete_confirm(request))


@api_view(['GET'])
def export_data(request):
    try:
        is_boy = request.GET['is_boy']
        return Service.export_data(is_boy)
    except Exception as e:
        return Response({
            "status": "fail",
            "data": str(e)
        })



@api_view(['POST'])
def admin_login(request):
    body = request.data
    username = body['username']
    password = body['password']
    result, error = Service.login_service(username, password)
    if error:
        return Response({
            "status": "fail",
            "data": str(result)
        })
    return Response({
        "status": "success",
        "data": {
            "username": result.username
        }
    })


@api_view(['GET'])
def get_all_customer(request):
    try:
        name = request.GET['name']
        is_boy = int(request.GET['is_boy'])
        page = request.GET['page']
        limit = request.GET['limit']
        customers, total_row, total_page = Service.get_customer(name, is_boy, page, limit)
        return Response({
            "status": "success",
            "data": {
                "customers": customers,
                "total_row": total_row,
                "page": int(page),
                "total_page": total_page
            }
        })
    except Exception as e:
        return Response({
            "status": "fail",
            "data": {
                "message": str(e)
            }
        })
