from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MedicalStaff, Address, Patient, NationCl025, TreatmentSession, Comorbidity, StageOfTreatment, \
    NationCl026, Surgery, SurgeryMedicalStaff, NationClPill, Pharmacotherapy, Physiotherapy, \
    PhysiotherapyMedicalStaff, ElectroUltrasoundTherapy, EusMedicalStaff, State, NationCl027, LaboratoryTest, \
    LabMedicalStaff, CatalogMeasurement, Measurement, Image
from .serializers import PatientSerializer, TreatmentSessionSerializer, StageOfTreatmentSerializer, \
    PharmacotherapySerializer, StateSerializer, LaboratoryTestSerializer


@api_view(['GET'])
def patientApiOverview(request):
    api_urls = {
        'List': '/patient-list/',
        'Detail View': '/patient-detail/<str:pk>/',
        'Create': '/patient-create/',
        'Update': '/patient-update/<str:pk>/',
        'Delete': '/patient-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def patientList(request):
    patients = Patient.objects.all().order_by('-id')
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def patientDetail(request, pk):
    patients = Patient.objects.get(id=pk)
    serializer = PatientSerializer(patients, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def patientCreate(request):
    serializer = PatientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def patientUpdate(request, pk):
    patient = Patient.objects.get(id=pk)
    serializer = PatientSerializer(instance=patient, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def patientDelete(request, pk):
    patient = Patient.objects.get(id=pk)
    patient.delete()
    return Response('Item was successfully delete!')


@api_view(['GET'])
def treatmentSessionApiOverview(request):
    api_urls = {
        'List': '/treatmentSession-list/',
        'Detail View': '/treatmentSession-detail/<str:pk>/',
        'Create': '/treatmentSession-create/',
        'Update': '/treatmentSession-update/<str:pk>/',
        'Delete': '/treatmentSession-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def treatmentSessionList(request):
    treatmentSessions = TreatmentSession.objects.all().order_by('-id')
    serializer = TreatmentSessionSerializer(treatmentSessions, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def treatmentSessionDetail(request, pk):
    treatmentSessions = TreatmentSession.objects.get(id=pk)
    serializer = TreatmentSessionSerializer(treatmentSessions, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def treatmentSessionCreate(request):
    serializer = TreatmentSessionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def treatmentSessionUpdate(request, pk):
    treatmentSession = TreatmentSession.objects.get(id=pk)
    serializer = TreatmentSessionSerializer(instance=treatmentSession, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def treatmentSessionDelete(request, pk):
    treatmentSession = TreatmentSession.objects.get(id=pk)
    treatmentSession.delete()
    return Response('Item was successfully delete!')


@api_view(['GET'])
def stageOfTreatmentApiOverview(request):
    api_urls = {
        'List': '/stageOfTreatment-list/',
        'Detail View': '/stageOfTreatment-detail/<str:pk>/',
        'Create': '/stageOfTreatment-create/',
        'Update': '/stageOfTreatment-update/<str:pk>/',
        'Delete': '/stageOfTreatment-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def stageOfTreatmentList(request):
    stageOfTreatments = StageOfTreatment.objects.all().order_by('-id')
    serializer = StageOfTreatmentSerializer(stageOfTreatments, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def stageOfTreatmentDetail(request, pk):
    stageOfTreatments = StageOfTreatment.objects.get(id=pk)
    serializer = StageOfTreatmentSerializer(stageOfTreatments, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def stageOfTreatmentCreate(request):
    serializer = StageOfTreatmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def stageOfTreatmentUpdate(request, pk):
    stageOfTreatment = StageOfTreatment.objects.get(id=pk)
    serializer = StageOfTreatmentSerializer(instance=stageOfTreatment, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def stageOfTreatmentDelete(request, pk):
    stageOfTreatment = StageOfTreatment.objects.get(id=pk)
    stageOfTreatment.delete()
    return Response('Item was successfully delete!')


@api_view(['GET'])
def pharmacotherapyApiOverview(request):
    api_urls = {
        'List': '/pharmacotherapy-list/',
        'Detail View': '/pharmacotherapy-detail/<str:pk>/',
        'Create': '/pharmacotherapy-create/',
        'Update': '/pharmacotherapy-update/<str:pk>/',
        'Delete': '/pharmacotherapy-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def pharmacotherapyList(request):
    pharmacotherapies = Pharmacotherapy.objects.all().order_by('-id')
    serializer = PharmacotherapySerializer(pharmacotherapies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def pharmacotherapyDetail(request, pk):
    pharmacotherapies = PharmacotherapySerializer.objects.get(id=pk)
    serializer = PharmacotherapySerializer(pharmacotherapies, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def pharmacotherapyCreate(request):
    serializer = PharmacotherapySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def pharmacotherapyUpdate(request, pk):
    pharmacotherapy = Pharmacotherapy.objects.get(id=pk)
    serializer = PharmacotherapySerializer(instance=pharmacotherapy, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def pharmacotherapyDelete(request, pk):
    pharmacotherapy = Pharmacotherapy.objects.get(id=pk)
    pharmacotherapy.delete()
    return Response('Item was successfully delete!')

@api_view(['GET'])
def stateApiOverview(request):
    api_urls = {
        'List': '/state-list/',
        'Detail View': '/state-detail/<str:pk>/',
        'Create': '/state-create/',
        'Update': '/state-update/<str:pk>/',
        'Delete': '/state-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def stateList(request):
    states = State.objects.all().order_by('-id')
    serializer = StateSerializer(states, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def stateDetail(request, pk):
    states = State.objects.get(id=pk)
    serializer = StateSerializer(states, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def stateCreate(request):
    serializer = StateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def stateUpdate(request, pk):
    state = State.objects.get(id=pk)
    serializer = StateSerializer(instance=state, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def stateDelete(request, pk):
    state = State.objects.get(id=pk)
    state.delete()
    return Response('Item was succsesfully delete!')

@api_view(['GET'])
def laboratoryTestApiOverview(request):
    api_urls = {
        'List': '/laboratoryTest-list/',
        'Detail View': '/laboratoryTest-detail/<str:pk>/',
        'Create': '/laboratoryTest-create/',
        'Update': '/laboratoryTest-update/<str:pk>/',
        'Delete': '/laboratoryTest-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def laboratoryTestList(request):
    laboratoryTests = LaboratoryTest.objects.all().order_by('-id')
    serializer = LaboratoryTestSerializer(laboratoryTests, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def laboratoryTestDetail(request, pk):
    laboratoryTests = LaboratoryTest.objects.get(id=pk)
    serializer = LaboratoryTestSerializer(laboratoryTests, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def laboratoryTestCreate(request):
    serializer = LaboratoryTestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def laboratoryTestUpdate(request, pk):
    laboratoryTest = LaboratoryTest.objects.get(id=pk)
    serializer = LaboratoryTestSerializer(instance=laboratoryTest, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def laboratoryTestDelete(request, pk):
    laboratoryTest = LaboratoryTest.objects.get(id=pk)
    laboratoryTest.delete()
    return Response('Item was successfully delete!')
