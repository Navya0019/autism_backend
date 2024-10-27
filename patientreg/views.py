from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Patient
from .serializers import PatientSerializer,PatientCheckSerializer

@api_view(['POST'])
def register_patient(request):
    serializer = PatientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()  # Save unique_id and other data directly
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyPatientView(APIView):
    def post(self, request):
        
        unique_id = request.data.get('unique_id')
        try:
            patient = Patient.objects.get(unique_id=unique_id)
            return Response({'message': 'Patient found', 'patient': patient.name}, status=status.HTTP_200_OK)
        except Patient.DoesNotExist:
            return Response({'message': 'Patient not found'}, status=status.HTTP_404_NOT_FOUND)