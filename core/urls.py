from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.http import JsonResponse

def api_welcome(request):
    return JsonResponse({
        "message": "Welcome to the Enterprise Task Manager API!",
        "status": "Production server is running smoothly.",
        "docs": "End points are available at /api/tasks/ and authentication at /api/auth/login/ and /api/auth/refresh/"
        })


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tasks/', include('tasks.urls')),
    path('', api_welcome, name='api_welcome'),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
