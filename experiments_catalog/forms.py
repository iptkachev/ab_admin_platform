from django.forms import ModelForm, DateInput, TextInput, Textarea, SelectDateWidget, SplitDateTimeWidget
from django.core.exceptions import ValidationError
from .models import Experiment


class ExperimentForm(ModelForm):
    class Meta:
        model = Experiment
        fields = "__all__"

        widgets = {
            'id_experiment': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
            'date_period_from': DateInput(attrs={'class': 'form-control'}, format='%Y-%m-%d'),
            'date_period_to': DateInput(attrs={'class': 'form-control'}, format='%Y-%m-%d'),
            'date_postperiod_to': DateInput(attrs={'class': 'form-control'}, format='%Y-%m-%d'),
            'target_camp_wave_ids': TextInput(attrs={'class': 'form-control'}),
            'control_camp_wave_id': TextInput(attrs={'class': 'form-control'}),
            'wave_ids': TextInput(attrs={'class': 'form-control'}),
        }

    def clean_id_experiment(self):
        new_id_experiment = self.cleaned_data['id_experiment'].lower()

        if new_id_experiment == 'create':
            raise ValidationError('Id experiment can not be "Create"')
        is_exist_id_experiment = Experiment.objects.filter(id_experiment__iexact=new_id_experiment).count()
        if is_exist_id_experiment:
            raise ValidationError(f'Id experiment must be unique. {new_id_experiment} already exists')
        return new_id_experiment
