from django.conf.urls import url
from myfile import views
urlpatterns=[
    url(r'^', views.kinomir, name="kinomir"),
]