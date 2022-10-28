
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users import views
urlpatterns = [
    path('signup/', views.UserView.as_view(), name='user_view'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]
#이렇게만 해도 views 만들어주지 않았는데 알아서 처리를 하는중