from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('getpdf/',views.get_PDF_page,name='getpdf'),
]