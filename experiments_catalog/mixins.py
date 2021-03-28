from .models import Experiment


class ExperimentViewMixin:
    model = Experiment
    context_object_name = 'experiment'
    slug_url_kwarg = 'id_experiment'
    slug_field = 'id_experiment'
