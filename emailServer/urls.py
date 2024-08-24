from django.urls import path

from emailServer import views

urlpatterns = [
    path("sendByFormEmail/", views.BasicEmailView.as_view(), name='send_email'),
    path("sendEmail/",views.BasicEmailView.sendEmail)
]