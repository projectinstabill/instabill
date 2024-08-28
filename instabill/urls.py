from django.contrib import admin
from django.urls import path
from bill.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', demo, name='demo'),

    path('', index, name='index'),
    path('login_page/', login_page, name='login_page'),
    path('logout_page/', logout_page, name='logout_page'),
    path('register/', register, name='register'),
    path('setup_profile/', setup_profile, name='setup_profile'),
    path('view_profile/', view_profile, name='view_profile'),
    path('update_profile/', update_profile, name='update_profile'),
    path('home/', home, name='home'),
    
    path('delete_profile/<int:pk>', update_profile, name='update_profile'),
    
    path('customer_create/', customer_create, name='customer_create'),
    path('customer_read/', customer_read, name='customer_read'),
    path('customer_update/<int:pk>/', customer_update, name='customer_update'),
    path('customer_delete/<int:pk>/', customer_delete, name='customer_delete'),
    
    path('supplier_create/', supplier_create, name='supplier_create'),
    path('supplier_read/', supplier_read, name='supplier_read'),
    path('supplier_update/<int:pk>/', supplier_update, name='supplier_update'),
    path('supplier_delete/<int:pk>/', supplier_delete, name='supplier_delete'),
    
    path('item_create/', item_create, name='item_create'),
    path('item_read/', item_read, name='item_read'),
    path('item_update/<int:pk>/', item_update, name='item_update'),
    path('item_delete/<int:pk>/', item_delete, name='item_delete'),
    
    path('invoice_create/', invoice_create, name='invoice_create'),
    path('invoice_read/', invoice_read, name='invoice_read'),
    path('invoice_billbook/', invoice_billbook, name='invoice_billbook'),
    path('invoice_print/<int:pk>/', invoice_print, name='invoice_print'),
    path('invoice_update/<int:pk>/', invoice_update, name='invoice_update'),
    path('invoice_delete/<int:pk>/', invoice_delete, name='invoice_delete'),

]
