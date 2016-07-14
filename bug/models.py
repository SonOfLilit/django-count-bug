from django.db import models

class A(models.Model):
    pass

class B(models.Model):
    a = models.ForeignKey(A)

class C(models.Model):
    a = models.ForeignKey(A)
