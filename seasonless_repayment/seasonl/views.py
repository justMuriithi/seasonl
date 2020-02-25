from seasonl.models import (
    Season, Customers, CustomerSummaries, RepaymentUploads, Repayments)
from seasonl.serializers import (SeasonSerializer, CustomersSerializer,
                                 CustomerSummariesSerializer,
                                 RepaymentUploadsSerializer,
                                 RepaymentsSerializer)
from rest_framework import viewsets


class SeasonViewSet(viewsets.ModelViewSet):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer


class CutomersViewSet(viewsets.ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer


class CutomerSummariesViewSet(viewsets.ModelViewSet):
    queryset = CustomerSummaries.objects.all()
    serializer_class = CustomerSummariesSerializer


class RepaymentUploadsViewSet(viewsets.ModelViewSet):
    queryset = RepaymentUploads.objects.all()
    serializer_class = RepaymentUploadsSerializer


class RepaymentsViewSet(viewsets.ModelViewSet):
    queryset = Repayments.objects.all()
    serializer_class = RepaymentsSerializer
