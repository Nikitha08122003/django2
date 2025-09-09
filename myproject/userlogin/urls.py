from django.urls import path
from. import views
urlpatterns=[
    path ('signup/',views.signup),
    path ('login/',views.userlogin),
    path ('use/',views.userd),
    path ('logout/',views.userlogout),




]