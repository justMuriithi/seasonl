from django.db import models

# Create your models here.


class Season(models.Model):
    SeasonName = models.CharField(max_length=100, blank=True, default='')
    StartDate = models.DateField()
    EndDate = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['StartDate']


class Customers(models.Model):
    CustomerName = models.CharField(max_length=100)


class CustomerSummaries(models.Model):
    CustomerID = models.ForeignKey(Customers, on_delete=models.CASCADE)
    SeasonID = models.ForeignKey(Season, on_delete=models.CASCADE)
    TotalRepaid = models.FloatField()
    TotalCredit = models.FloatField()


class RepaymentUploads(models.Model):
    CustomerID = models.ForeignKey(Customers, on_delete=models.CASCADE)
    SeasonID = models.ForeignKey(
        Season, on_delete=models.CASCADE, blank=True, null=True)
    Date = models.DateField()
    Amount = models.FloatField()


class Repayments(models.Model):
    CustomerID = models.ForeignKey(Customers, on_delete=models.CASCADE)
    SeasonID = models.ForeignKey(
        Season, on_delete=models.CASCADE, blank=True, null=True)
    Date = models.DateField()
    Amount = models.FloatField()
    ParentID = models.IntegerField(blank=True, null=True)
