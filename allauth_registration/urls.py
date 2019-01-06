from django.conf.urls import url
from django.urls import path
from . import views as registrationviews
from django.contrib.auth import views as djangoviews
from allauth.account.views import EmailView as allauth_AccountEmail



urlpatterns=[
    path('', registrationviews.home, name='home'),
    path('secret/',registrationviews.secret_page,name='secret'),
    path('accounts/email/',allauth_AccountEmail.as_view(),name='account_email'),

]

