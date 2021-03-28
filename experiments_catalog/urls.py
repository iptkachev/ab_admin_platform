from django.urls import path
from .views import *

urlpatterns = [
    path('', ExperimentsCatalog.as_view(), name='experiments_catalog_url'),
    path('experiment/create', ExperimentCreate.as_view(), name='experiment_create_url'),
    path('experiment/<slug:id_experiment>', ExperimentDetail.as_view(), name='experiment_detail_url'),
    path('experiment/<slug:id_experiment>/update', ExperimentUpdate.as_view(), name='experiment_update_url'),
    path('experiment/<slug:id_experiment>/delete', ExperimentDelete.as_view(), name='experiment_delete_url')
]
