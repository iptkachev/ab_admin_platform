from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.shortcuts import reverse


# Create your models here.
class Experiment(models.Model):
    id_experiment = models.SlugField(max_length=50, unique=True)
    description = models.CharField(max_length=150, blank=True, db_index=True)
    date_period_from = models.DateField()
    date_period_to = models.DateField()
    date_postperiod_to = models.DateField()
    target_camp_wave_ids = ArrayField(models.PositiveIntegerField(), size=10)
    control_camp_wave_id = models.PositiveIntegerField()
    wave_ids = ArrayField(models.PositiveIntegerField(), size=10)

    def get_detail_url(self):
        return reverse('experiment_detail_url', kwargs={'id_experiment': self.id_experiment})

    def get_update_url(self):
        return reverse('experiment_update_url', kwargs={'id_experiment': self.id_experiment})

    def get_delete_url(self):
        return reverse('experiment_delete_url', kwargs={'id_experiment': self.id_experiment})

    def __str__(self):
        return f'{self.id_experiment}'
