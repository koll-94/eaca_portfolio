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


class FileExpansion(models.Model):
    type_file = models.TextField(max_length=200)


class Files(models.Model):
    file_str = models.TextField(max_length=200)
    file_expansion = models.ForeignKey(FileExpansion)


class DocType(models.Model):
    name = models.TextField(max_length=250, blank=True)
    abbr = models.TextField(max_length=50, blank=True, null=True)


class DocSubType(models.Model):
    name = models.TextField(max_length=200)


class Document(models.Model):
    doc_type = models.ForeignKey(DocType)
    user = models.ForeignKey(User)
    sub_type = models.ForeignKey(DocSubType, blank=True, default=None)
    file = models.ForeignKey(Files, blank=True, default=None)


class DocStructure(models.Model):
    type = models.CharField(max_length=50, null=True, default='string')
    doc_type = models.ForeignKey(DocType)
    name = models.TextField(max_length=400)


class DocField(models.Model):
    doc_id = models.ForeignKey(Document)
    value = models.TextField(max_length=400)
    doc_str = models.ForeignKey(DocStructure)


class Profile(models.Model):
    user_id = models.ForeignKey(User)
    uch_step = models.TextField(max_length=200)
    uch_zvan = models.TextField(max_length=200)
    dolgnost = models.TextField(max_length=200)
    kval = models.TextField(max_length=200)
    experience_all = models.IntegerField()
    experience_spec = models.IntegerField()
    experience_eaca = models.IntegerField()
    disser_job = models.TextField(max_length=200)
    sience_inter = models.TextField(max_length=200)


