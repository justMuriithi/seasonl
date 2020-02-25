from rest_framework import serializers
from seasonl.models import (Season, Customers, CustomerSummaries, Repayments,
                            RepaymentUploads)


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ['SeasonName', 'StartDate', 'EndDate']


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['CustomerName']


class CustomerSummariesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerSummaries
        fields = ['CustomerID', 'SeasonID', 'TotalRepaid', 'TotalCredit']


class RepaymentUploadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepaymentUploads
        fields = ['CustomerID', 'SeasonID', 'Date', 'Amount']


class RepaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repayments
        fields = ['CustomerID',
                  'SeasonID', 'Date', 'Amount', 'ParentID']
