
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
    path('community/', include('community.urls')),
    path('accounts/', include('accounts.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),    
]
