from django.urls import path
from myapp import views
urlpatterns=[
    path("result/",views.myfunction),
    path('html/',views.mydemo),
    path('forms/',views.formshow),
    path('leo/',views.data),
    path('update/<int:id>/',views.update,name="update"),
    path('delete/<int:id>/',views.delete,name="delete"),



]