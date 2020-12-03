from django.urls import path
from . import views


urlpatterns = [

    path('patient', views.patientApiOverview, name="patient-api-overview"),
    path('patient-list/', views.patientList, name="patient-list"),
    path('patient-detail/<str:pk>/', views.patientDetail, name="patient-detail"),
    path('patient-create/', views.patientCreate, name="patient-create"),
    path('patient-update/<str:pk>/', views.patientUpdate, name="patient-update"),
    path('patient-delete/<str:pk>/', views.patientDelete, name="patient-delete"),

    path('treatmentSession', views.treatmentSessionApiOverview, name="treatmentSession-api-overview"),
    path('treatmentSession-list/', views.treatmentSessionList, name="treatmentSession-list"),
    path('treatmentSession-detail/<str:pk>/', views.treatmentSessionDetail, name="treatmentSession-detail"),
    path('treatmentSession-create/', views.treatmentSessionCreate, name="treatmentSession-create"),
    path('treatmentSession-update/<str:pk>/', views.treatmentSessionUpdate, name="treatmentSession-update"),
    path('treatmentSession-delete/<str:pk>/', views.treatmentSessionDelete, name="treatmentSession-delete"),

    path('stageOfTreatment', views.stageOfTreatmentApiOverview, name="stageOfTreatment-api-overview"),
    path('stageOfTreatment-list/', views.stageOfTreatmentList, name="stageOfTreatment-list"),
    path('stageOfTreatment-detail/<str:pk>/', views.stageOfTreatmentDetail, name="stageOfTreatment-detail"),
    path('stageOfTreatment-create/', views.stageOfTreatmentCreate, name="stageOfTreatment-create"),
    path('stageOfTreatment-update/<str:pk>/', views.stageOfTreatmentUpdate, name="stageOfTreatment-update"),
    path('stageOfTreatment-delete/<str:pk>/', views.stageOfTreatmentDelete, name="stageOfTreatment-delete"),

    path('pharmacotherapy', views.pharmacotherapyApiOverview, name="pharmacotherapy-api-overview"),
    path('pharmacotherapy-list/', views.pharmacotherapyList, name="pharmacotherapy-list"),
    path('pharmacotherapy-detail/<str:pk>/', views.pharmacotherapyDetail, name="pharmacotherapy-detail"),
    path('pharmacotherapy-create/', views.pharmacotherapyCreate, name="pharmacotherapy-create"),
    path('pharmacotherapy-update/<str:pk>/', views.pharmacotherapyUpdate, name="pharmacotherapy-update"),
    path('pharmacotherapy-delete/<str:pk>/', views.pharmacotherapyDelete, name="pharmacotherapy-delete"),

    path('state', views.stateApiOverview, name="state-api-overview"),
    path('state-list/', views.stateList, name="state-list"),
    path('state-detail/<str:pk>/', views.stateDetail, name="state-detail"),
    path('state-create/', views.stateCreate, name="state-create"),
    path('state-update/<str:pk>/', views.stateUpdate, name="state-update"),
    path('state-delete/<str:pk>/', views.stateDelete, name="state-delete"),

    path('laboratoryTest', views.laboratoryTestApiOverview, name="laboratoryTest-api-overview"),
    path('laboratoryTest-list/', views.laboratoryTestList, name="laboratoryTest-list"),
    path('laboratoryTest-detail/<str:pk>/', views.laboratoryTestDetail, name="laboratoryTest-detail"),
    path('laboratoryTest-create/', views.laboratoryTestCreate, name="laboratoryTest-create"),
    path('laboratoryTest-update/<str:pk>/', views.laboratoryTestUpdate, name="laboratoryTest-update"),
    path('laboratoryTest-delete/<str:pk>/', views.laboratoryTestDelete, name="laboratoryTest-delete"),
]
