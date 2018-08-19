# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        """Return a string representation of the model."""
        return self.text


class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __unicode__(self):
        """Return a string representation of the model."""
        return self.text[:50] + "..."
