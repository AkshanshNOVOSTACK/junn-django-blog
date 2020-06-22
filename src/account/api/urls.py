from django.urls import path
from account.api.views import (
    registration_view,
    account_properties_view,
    account_update_view,
    ObtainAuthTokenView
)


app_name='account'

urlpatterns =[
    path('login', ObtainAuthTokenView.as_view(), name='login'),
    path('properties', account_properties_view, name='properties'),
    path('properties/update', account_update_view, name='update'),
    path('register', registration_view, name='registration'),
    path('register', registration_view, name='registration'),
]