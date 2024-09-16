from django.urls import path
from . import views

urlpatterns = [
    path('', views.endpoints),
    path('advocates/', views.advocates_list, name = "advocates_url"),
    # path('advocates/<str:username>/', views.advocates_details)
    path('advocates/<str:username>/', views.AdvocateDetails.as_view())
]