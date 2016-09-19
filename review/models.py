from __future__ import unicode_literals

from django.db import models

# Create your models here.
class inputFrom(models.Model):
    patchNumber = models.DecimalField(max_digits=10, decimal_places=1, unique=True)

    condition = models.TextField()
    issue = models.TextField()
    freq = models.CharField(max_length=10)
    branchMain = models.CharField(max_length=15)
    reportDoc = models.CharField(max_length=50)
    issueGrade = models.CharField(max_length=10)

    testCase = models.TextField()
    sideEffect = models.TextField()
    qaUser  = models.CharField(max_length=15)
    testUser = models.CharField(max_length=15)
    engineerUser = models.CharField(max_length=15)
    funcClass = models.CharField(max_length=15)
    region = models.CharField(max_length=15)

    issueDate = models.DateField()
    issueClass = models.CharField(max_length=15)
    issuePlace = models.CharField(max_length=15)

    isCLCA = models.BooleanField()
    contentsCLCA = models.CharField(max_length=20)

    now = models.DateTimeField(auto_now_add=True)