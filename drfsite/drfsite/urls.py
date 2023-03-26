"""drfsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from women.views import *
from rest_framework import routers
from women.routers import MyCustomRouter


# SimpleRouter
# router = routers.SimpleRouter()
# router.register(r'women', WomenViewSet)

# # роутер формирует список маршрутов и связывает их с определенным ViewSet
# # в отличие от SimpleRouter, DefaultRouter имеет адрес общего api, со ссылками на остальные
# # router = routers.DefaultRouter()
# router = MyCustomRouter()
# # префикс (basename) имени маршрута формируется из имени модели в queryset
# router.register(r'women', WomenViewSet)
# # # вариант с вводом префикса вручную (обязательно требуется, если не задан queryset во View
# # router.register(r'women', WomenViewSet, basename='men')
# print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),

    # 11 Auth
    path('api/v1/drf-auth/', include('rest_framework.urls')),

    # 10 Permissions
    path('api/v1/women/', WomenAPIList.as_view()),
    path('api/v1/women/<int:pk>/', WomenAPIUpdate.as_view()),
    path('api/v1/womendelete/<int:pk>/', WomenAPIDestroy.as_view()),

    # 12 Djoser
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    # 13 JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # 9 Маршруты для ViewSet через роутер
    # http://127.0.0.1:8000/api/v1/women/, # http://127.0.0.1:8000/api/v1/women/<pk>
    # path('api/v1/', include(router.urls)),


    # 8 Маршруты для ViewSet стандартным способом
    # path('api/v1/womenlist/', WomenViewSet.as_view({'get': 'list'})),
    # path('api/v1/womenlist/<int:pk>/', WomenViewSet.as_view({'put': 'update'})),

    # Маршуты для APIView
    # path('api/v1/womenlist/', WomenAPIList.as_view()),
    # path('api/v1/womenlist/<int:pk>/', WomenAPIUpdate.as_view()),
    # path('api/v1/womendetail/<int:pk>/', WomenAPIDetailView.as_view()),
]
