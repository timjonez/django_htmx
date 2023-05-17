from django.contrib import admin
from . import models

admin.site.register(models.Project)
admin.site.register(models.ProjectPicture)
admin.site.register(models.Technology)
