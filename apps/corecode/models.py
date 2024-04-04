from django.db import models
from apps.staffs.models import Staff
# Create your models here.


class SiteConfig(models.Model):
    """Site Configurations"""

    key = models.SlugField()
    value = models.CharField(max_length=200)

    def __str__(self):
        return self.key

class Subject(models.Model):
    """Subject"""

    name = models.CharField(max_length=200, unique=True)
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class StudentClass(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"
        ordering = ["name"]

    def __str__(self):
        return self.name
