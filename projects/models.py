from django.db import models


class Project(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=63)
    sub_title = models.CharField(max_length=127)
    live_link = models.URLField(null=True, blank=True)
    source_link = models.URLField()
    description = models.TextField()


class Technology(models.Model):
    name = models.CharField(max_length=63)
    image = models.ImageField(null=True, blank=True)
    projects = models.ManyToManyField(Project, related_name='technologies')


class ProjectPicture(models.Model):
    title = models.CharField(max_length=127)
    image = models.ImageField()
    project = models.ForeignKey(
        Project, related_name='pictures', on_delete=models.CASCADE)
