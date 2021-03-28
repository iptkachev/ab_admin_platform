from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse_lazy
from .models import Experiment
from .forms import ExperimentForm
from .mixins import ExperimentViewMixin
# Create your views here.


@method_decorator(login_required, name='dispatch')
class ExperimentsCatalog(ListView):
    model = Experiment
    template_name = 'experiments_catalog/index.html'
    context_object_name = 'experiments'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        experiments = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(experiments, self.paginate_by)

        try:
            experiments = paginator.page(page)
        except PageNotAnInteger:
            experiments = paginator.page(1)
        except EmptyPage:
            experiments = paginator.page(paginator.num_pages)

        context['experiments'] = experiments
        return context


@method_decorator(login_required, name='dispatch')
class ExperimentDetail(ExperimentViewMixin, DetailView):
    template_name = 'experiments_catalog/detail.html'


@method_decorator(login_required, name='dispatch')
class ExperimentCreate(ExperimentViewMixin, CreateView):
    form_class = ExperimentForm
    template_name = 'experiments_catalog/create.html'
    success_url = reverse_lazy('experiments_catalog_url')


@method_decorator(login_required, name='dispatch')
class ExperimentUpdate(ExperimentViewMixin, UpdateView):
    fields = [field.name for field in Experiment._meta.get_fields() if field.name != 'id_experiment']
    template_name = 'experiments_catalog/update.html'

    def get_success_url(self):
        return reverse_lazy('experiment_detail_url', kwargs={'id_experiment': self.object.id_experiment})


@method_decorator(login_required, name='dispatch')
class ExperimentDelete(ExperimentViewMixin, DeleteView):
    template_name = 'experiments_catalog/delete.html'
    success_url = reverse_lazy('experiments_catalog_url')
