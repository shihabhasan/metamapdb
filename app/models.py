# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class QueryTable(models.Model):
    queryid = models.TextField(primary_key=True)
    mappcount = models.IntegerField()
    unmappcount = models.IntegerField()

    domain = models.TextField()
    phylum = models.TextField()
    taxoclass = models.TextField()
    order = models.TextField()
    family = models.TextField()
    genus = models.TextField()
    species = models.TextField()

    domainCount = models.IntegerField()
    phylumCount = models.IntegerField()
    taxoclassCount = models.IntegerField()
    orderCount = models.IntegerField()
    familyCount = models.IntegerField()
    genusCount = models.IntegerField()
    speciesCount = models.IntegerField()

    domainSensitivity = models.FloatField()
    phylumSensitivity = models.FloatField()
    taxoclassSensitivity = models.FloatField()
    orderSensitivity = models.FloatField()
    familySensitivity = models.FloatField()
    genusSensitivity = models.FloatField()
    speciesSensitivity = models.FloatField()

    def __str__(self):
        return self.queryid


class ReferenceTable(models.Model):
    refernceid = models.TextField(primary_key=True)
    domain = models.TextField()
    phylum = models.TextField()
    taxoclass = models.TextField()
    order = models.TextField()
    family = models.TextField()
    genus = models.TextField()
    species = models.TextField()

    def __str__(self):
        return self.refernceid