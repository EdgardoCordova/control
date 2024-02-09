from django.urls import path
from .views import (
    DescriptionsListView, 
    CircuitDescriptionUpdateView,
    circuit_descriptions_generation_view,
    circuit_descriptions_run_view
)

app_name = 'descriptions'

urlpatterns = [
    path('', DescriptionsListView.as_view(), name='main'),
    path('update/<int:pk>', CircuitDescriptionUpdateView.as_view() , name='circuit-description-update'),
    path('generation/<int:pk>', circuit_descriptions_generation_view , name='circuit-descriptions-generation'),
    path('run/<int:pk>', circuit_descriptions_run_view , name='generation-run'),

]