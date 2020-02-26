from django.urls import path, include
from rest_framework.routers import DefaultRouter
from seasonl import views

router = DefaultRouter()
router.register(r'seasons', views.SeasonViewSet)
router.register(r'customers', views.CutomersViewSet)
router.register(r'customersummaries', views.CutomerSummariesViewSet)
router.register(r'repaymentuploads', views.RepaymentUploadsViewSet)
router.register(r'repayments', views.RepaymentsViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
