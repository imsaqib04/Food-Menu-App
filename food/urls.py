from . import views
from django.urls import path

app_name  = 'food'
urlpatterns = [
    #/food/
    path("",views.index,name = "index"),
    #/food/1
    path("<int:item_id>/",views.details,name = "detail"),
    path("item/",views.item,name = "item"),
]
