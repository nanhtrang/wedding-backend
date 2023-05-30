from django.urls import path, include
from . import views

urlpatterns = [
    path('method-wish', view=views.method_wish, name="method_wish"),
    path('confirm', view=views.method_confirm, name="method_confirm"),
    path('export', view=views.export_data, name="export"),
    path('login', view=views.admin_login, name="login"),
    path('getCustomer', view=views.get_all_customer, name="getAllCustomer"),
    path('getCustomer/<int:id>', view=views.method_confirm, name="method_confirm_delete"),
]
