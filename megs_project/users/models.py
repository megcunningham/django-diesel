# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
        
        
# Workout Models     
        
class MuscleGroup(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
    return self

class Workouts(models.Model):
    group_name = models.ForeignKey(MuscleGroup)
    collection = models.ForeignKey(Exercise.name)
    
    def __str__(self):
        return self
    
class Exercise(models.Model):
     name = models.CharField(max_length=25)
     sets = models.ForeignKey(Set)
    
    def __str__(self):
        return self.name
                
class Set(models.model):
    set_number = models.CharField(max_length=2)
    weight = models.Charfield(max_length=40)
    reps = models.CharField(max_length=20)
    notes = models.CharField(max_length=200)
    
    def __str__(self):
        return self
        

        

    


