from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Organization(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Command(models.Model):
    command = models.CharField(max_length=30, unique=True)
    min_arg = models.SmallIntegerField(null=True, blank=True)
    max_arg = models.SmallIntegerField(null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    detail_description = models.CharField(max_length=4000, null=True, blank=True)
    long_command = models.BooleanField(default=False)
    to_log = models.BooleanField(default=True)
    enabled = models.BooleanField(default=False)
    interactive = models.BooleanField(default=False)
    py_module = models.CharField(max_length=150)
    py_routine = models.CharField(max_length=150)

    def __str__(self):
        return self.command

    class Meta:
        ordering = ('command',)


class Role(models.Model):
    role = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=200, blank=True)
    commands = models.ManyToManyField(Command)

    def __str__(self):
        return self.role

    class Meta:
        ordering = ('role',)


class TGUser(models.Model):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    enabled = models.BooleanField(default=False)
    tgid = models.PositiveIntegerField()
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
