from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.endpoints),
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('handles/', views.handles_list, name = "handle_url"),
    # path('handles/<str:username>/', views.advocates_details)
    path('handles/<str:username>/', views.HandleDetails.as_view()),

    #interests endpoint
    path('categories/', views.category_list)

]