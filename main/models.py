# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Chair(models.Model):
    abbr = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=200)


class ChairUser(models.Model):
    chair = models.ForeignKey(Chair)
    user = models.ForeignKey(User)


class DocType(models.Model):
    name = models.TextField(max_length=250, blank=True)
    abbr = models.TextField(max_length=50, default='')
    desc = models.TextField(max_length=200)


class Document(models.Model):
    user = models.ForeignKey(User)
    doc_type = models.ForeignKey(DocType)
    name = models.TextField(max_length=300)
    year = models.DateField(default='1970-01-01')


class FileExpansion(models.Model):
    type_file = models.TextField(max_length=200)


class Files(models.Model):
    file_str = models.TextField(max_length=200)
    file_expansion = models.ForeignKey(FileExpansion)


class DocFile(models.Model):
    doc = models.ForeignKey(Document)
    files = models.ForeignKey(Files)
