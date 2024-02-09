from django.urls import path
from .views import (
    CircuitsListView, 
    CircuitDescriptionsListView,
    CircuitUpdateView,
    
)

app_name = 'circuits'

urlpatterns = [
    path('', CircuitsListView.as_view(), name='main'),
    path('list/<pk>', CircuitDescriptionsListView.as_view() , name='circuit-descriptions-list'),
    path('update/<int:pk>', CircuitUpdateView.as_view() , name='circuit-update'),
    

]

