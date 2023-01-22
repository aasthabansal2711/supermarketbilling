from django.urls import path, include
from rest_framework import routers
from .views import ItemViewSet
from .views import ItemCreateView
from .views import ItemUpdateView


router = routers.DefaultRouter()
router.register('items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('items/', ItemCreateView.as_view(), name='create-item'),
    path('items/<int:id>', ItemUpdateView.as_view(), name='update-item'),
]