import os
from django.core.files import File
from rest_framework.response import Response
from .models import Wish, Confirm, Account
from django.forms.models import model_to_dict
import csv
from django.http import HttpResponse
from datetime import datetime


class Service():
    @classmethod
    def get_all_wish(cls):
        query_set = Wish.objects.all().order_by('-id')
        return {
            "status": "success",
            "data": query_set.values()
        }

    @classmethod
    def add_wish(cls, request):
        try:
            name = request.data['name']
            wish = request.data['wish']
            if name.strip() == '' or wish.strip() == '':
                raise Exception('name or wish is null')
            the_wish = Wish(name=name, wish=wish)
            the_wish.save()
            query_set = Wish.objects.all().order_by('-id')
            return {
                "status": "success",
                "data": {
                    "list": query_set.values(),
                    "wish": model_to_dict(the_wish)
                }
            }
        except Exception as e:
            return {
                "status": "fail",
                "data": str(e)
            }

    @classmethod
    def delete_wish(cls, request):
        try:
            id = request.data['id']
            the_wish = Wish.objects.get(id=id)
            the_wish.delete()
            query_set = Wish.objects.all().order_by('-id')
            return {
                "status": "success",
                "data": {
                    "list": query_set.values(),
                }
            }
        except Exception as e:
            return {
                "status": "fail",
                "data": str(e)
            }

    @classmethod
    def add_confirm(cls, request):
        try:
            name = request.data['name']
            number = request.data['number']
            addition = request.data['addition']
            if name.strip() == '' or number is None:
                raise Exception('name or wish is null')
            confirm = Confirm(name=name, number=number, isGroomSide=addition)
            confirm.save()
            return {
                "status": "success",
                "data": model_to_dict(confirm)
            }
        except Exception as e:
            return {
                "status": "fail",
                "data": str(e)
            }

    @classmethod
    def delete_confirm(cls, request):
        try:
            id = request.data['id']
            if id is None:
                raise Exception('id is null')
            confirm = Confirm.objects.get(id=id)
            confirm.delete()
            confirms = Confirm.objects.all().order_by('-id')
            return {
                "status": "success",
                "data": confirms.values()
            }
        except Exception as e:
            return {
                "status": "fail",
                "data": str(e)
            }


    @classmethod
    def get_all_confirm(cls):
        try:
            confirms = Confirm.objects.all().order_by('-id')
            return {
                "status": "success",
                "data": confirms.values()
            }
        except Exception as e:
            return {
                "status": "fail",
                "data": str(e)
            }

    @classmethod
    def export_data(cls, is_boy='0'):
        is_boy = int(is_boy)
        customers = None
        if is_boy == 0:
            customers = Confirm.objects.all().values()
        elif is_boy == 1:
            customers = Confirm.objects.filter(isGroomSide=True).values()
        else:
            customers = Confirm.objects.filter(isGroomSide=False).values()
        time = datetime.now().timestamp()
        response = HttpResponse(
            content_type="text/csv",
            headers={"Content-Disposition": 'attachment; filename="khach_moi_' + str(time) + '.csv"'},
        )

        writer = csv.writer(response)
        writer.writerow(["STT", "Tên", "Số lượng người", "Bạn của"])
        index = 1
        for item in customers:
            writer.writerow([str(index), item['name'], item['number'], 'Chú rể' if item['isGroomSide'] else 'Cô dâu'])
            index = index + 1

        return response

    @classmethod
    def login_service(cls, username, password):
        try:
            account = Account.objects.get(username=username, password=password)
            return account, None
        except Exception as e:
            return e, True


    @classmethod
    def get_customer(cls, name="", is_boy='0', page='0', limit='10'):
        pg = int(page)
        lmt = int(limit)
        offset = pg * lmt
        customers = None
        total_row = Confirm.objects.all().filter(name__contains=name).count()
        if is_boy == 0:
            total_row = Confirm.objects.all().filter(name__contains=name).count()
        elif is_boy == 1:
            total_row = Confirm.objects.all().filter(isGroomSide=True, name__contains=name).count()
        else:
            total_row = Confirm.objects.all().filter(isGroomSide=False, name__contains=name).count()
        total_page = int(total_row / lmt) + (1 if total_row % lmt > 0 else 0)
        if pg < 0 or pg > total_page:
            raise Exception("Page " + page + " is not valid")
        if is_boy == 0:
            customers = Confirm.objects.all().filter(name__contains=name)[offset:offset+lmt].values()
        elif is_boy == 1:
            customers = Confirm.objects.filter(isGroomSide=True, name__contains=name)[offset:offset+lmt].values()
        else:
            customers = Confirm.objects.filter(isGroomSide=False, name__contains=name)[offset:offset+lmt].values()
        return customers, total_row, total_page