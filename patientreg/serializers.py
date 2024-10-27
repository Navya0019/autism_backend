from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['unique_id', 'name', 'age', 'gender']
class PatientCheckSerializer(serializers.Serializer):
    patient_id = serializers.CharField(required=True)