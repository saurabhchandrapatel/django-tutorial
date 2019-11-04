from django.contrib import admin
# Register your models here.
from django.utils.html import format_html
from django.urls import path
from django.shortcuts import render
from django.conf.urls import url
from guardian.admin import GuardedModelAdmin


class CommonAdmin(GuardedModelAdmin):
	...