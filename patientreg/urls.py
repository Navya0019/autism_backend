from django.urls import path
from .views import register_patient,VerifyPatientView

urlpatterns = [
    path('verify-patient/', VerifyPatientView.as_view(), name='verify_patient'),
    path('register/', register_patient, name='register_patient'),
]
