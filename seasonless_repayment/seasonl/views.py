from seasonl.models import (
    Season, Customers, CustomerSummaries, RepaymentUploads, Repayments)
from seasonl.serializers import (SeasonSerializer, CustomersSerializer,
                                 CustomerSummariesSerializer,
                                 RepaymentUploadsSerializer,
                                 RepaymentsSerializer)
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


class SeasonViewSet(viewsets.ModelViewSet):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer


class CutomersViewSet(viewsets.ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer


class CutomerSummariesViewSet(viewsets.ModelViewSet):
    queryset = CustomerSummaries.objects.all()
    serializer_class = CustomerSummariesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['CustomerID']


class RepaymentUploadsViewSet(viewsets.ModelViewSet):
    queryset = RepaymentUploads.objects.all()
    serializer_class = RepaymentUploadsSerializer

    def perform_create(self, serializer):
        CustomerID = self.request.data['CustomerID']
        amount = self.request.data['Amount']
        season = self.request.data['SeasonID']
        Date = self.request.data['Date']
        # obtain all instances of debt
        records = CustomerSummaries.objects.filter(
            CustomerID=CustomerID).values()
        records_ = CustomerSummaries.objects.filter(
            CustomerID=CustomerID)
        loopcount = len(records)

        for n in range(0, loopcount):
            owed = float(records[n]['TotalCredit']) - \
                float(records[n]['TotalRepaid'])
            if season is not None:
                new_TotalRepaid = float(
                    records[n]['TotalRepaid']) + float(amount)
            elif float(amount) > owed:
                new_TotalRepaid = float(records[n]['TotalCredit'])
                new_amount = float(amount) - owed
                print("To be used to settle next season is ", new_amount)
                print("total repaid updated to", new_TotalRepaid)
            elif float(amount) == owed:
                new_TotalRepaid = float(records[n]['TotalCredit'])
                print("Debt for season settled")
            else:
                new_TotalRepaid = float(
                    records[n]['TotalRepaid']) + float(amount)
                print("Debt reduced.Total paid is ", new_TotalRepaid)

        serializer.save()

        # updating customer summaries
        customersummaries_serializer = CustomerSummariesSerializer(
            records_[n], data={"TotalRepaid": new_TotalRepaid}, partial=True)
        customersummaries_serializer.is_valid()
        customersummaries_serializer.save()

        # updating repayments table
        parentID = None
        repayment_data = {
            "CustomerID": CustomerID,
            "SeasonID": records[n]['SeasonID_id'],
            "Amount": amount,
            "Date": Date,
            "ParentID": parentID
        }
        repayments_serializer = RepaymentsSerializer(data=repayment_data)
        repayments_serializer.is_valid()
        repayments_serializer.save()

        parentID = repayments_serializer.data['id']


class RepaymentsViewSet(viewsets.ModelViewSet):
    queryset = Repayments.objects.all()
    serializer_class = RepaymentsSerializer
