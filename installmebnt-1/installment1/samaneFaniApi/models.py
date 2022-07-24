from django.db import models

# Create your models here.


class CallInstallment(models.Model):
    amount = models.CharField(max_length=100)
    controlCodeResult = models.CharField(max_length=100)
    installmentDate = models.CharField(max_length=8)
    insuredName = models.CharField(max_length=100)
    paymentStatus = models.CharField(max_length=100)
    policyNo = models.CharField(max_length=100)
    shenasepardakht = models.CharField(max_length=100)
