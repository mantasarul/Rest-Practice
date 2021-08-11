from django.urls import path
from django.urls.conf import include
from rest_framework.generics import GenericAPIView
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', views.ArticleViewSet, basename='article')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    path('article/', views.ArticleAPIView.as_view()),
    path('detail/<int:id>', views.ArticleDetails.as_view()),
    path('generic/article/<int:id>/', views.GenericAPIView.as_view()),
    path('generic/article/', views.GenericList.as_view()),
]
