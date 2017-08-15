# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class QueryTable(models.Model):
    queryid = models.TextField(primary_key=True)
    mappcount = models.IntegerField(null=True)
    unmappcount = models.IntegerField(null=True)

    domain = models.TextField(null=True)
    phylum = models.TextField(null=True)
    taxoclass = models.TextField(null=True)
    order = models.TextField(null=True)
    family = models.TextField(null=True)
    genus = models.TextField(null=True)
    species = models.TextField(null=True)

    domainCount = models.IntegerField(null=True)
    phylumCount = models.IntegerField(null=True)
    taxoclassCount = models.IntegerField(null=True)
    orderCount = models.IntegerField(null=True)
    familyCount = models.IntegerField(null=True)
    genusCount = models.IntegerField(null=True)
    speciesCount = models.IntegerField(null=True)

    domainSensitivity = models.FloatField(null=True)
    phylumSensitivity = models.FloatField(null=True)
    taxoclassSensitivity = models.FloatField(null=True)
    orderSensitivity = models.FloatField(null=True)
    familySensitivity = models.FloatField(null=True)
    genusSensitivity = models.FloatField(null=True)
    speciesSensitivity = models.FloatField(null=True)

    def __str__(self):
        return self.queryid


class ReferenceTable(models.Model):
    refernceid = models.TextField(primary_key=True)
    domain = models.TextField(null=True)
    phylum = models.TextField(null=True)
    taxoclass = models.TextField(null=True)
    order = models.TextField(null=True)
    family = models.TextField(null=True)
    genus = models.TextField(null=True)
    species = models.TextField(null=True)

    def __str__(self):
        return self.refernceid