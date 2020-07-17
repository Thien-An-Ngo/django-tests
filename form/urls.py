from django.urls import path

from . import views
# form app urls

urlpatterns = [
    path("", views.form, name="form")
]
