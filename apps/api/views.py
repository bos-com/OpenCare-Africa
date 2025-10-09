"""
API views for OpenCare-Africa health system.
"""

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model

from apps.api.permissions import IsClinicalStaff
from apps.records.models import HealthRecord
from apps.records.serializers import (
    HealthRecordCreateSerializer,
    HealthRecordDetailSerializer,
    HealthRecordSerializer,
)
from apps.records.filters import HealthRecordFilter

User = get_user_model()

# Import models (these will be created in their respective apps)
# from apps.patients.models import Patient, PatientVisit
# from apps.core.models import User, HealthFacility
# from apps.records.models import HealthRecord

# Import serializers (these will be created in their respective apps)
# from apps.patients.serializers import PatientSerializer, PatientVisitSerializer
# from apps.core.serializers import UserSerializer, HealthFacilitySerializer
# from apps.records.serializers import HealthRecordSerializer


class PatientViewSet(viewsets.ModelViewSet):
    """
    ViewSet for patient management.
    """
    permission_classes = [IsAuthenticated]
    queryset = User.objects.none()  # Placeholder until Patient model is implemented
    # serializer_class = PatientSerializer
    
    @action(detail=False, methods=['get'])
    def search(self, request):
        """Search patients by name, ID, or other criteria."""
        query = request.query_params.get('q', '')
        # patients = Patient.objects.filter(
        #     Q(first_name__icontains=query) | 
        #     Q(last_name__icontains=query) | 
        #     Q(patient_id__icontains=query)
        # )
        return Response({
            'message': 'Patient search endpoint',
            'query': query,
            'results': []  # patients
        })


class HealthWorkerViewSet(viewsets.ModelViewSet):
    """
    ViewSet for health worker management.
    """
    permission_classes = [IsAuthenticated]
    queryset = User.objects.filter(user_type__in=['doctor', 'nurse', 'midwife', 'community_worker'])
    # serializer_class = UserSerializer
    
    @action(detail=False, methods=['get'])
    def by_specialization(self, request):
        """Get health workers by specialization."""
        specialization = request.query_params.get('specialization', '')
        return Response({
            'message': 'Health workers by specialization endpoint',
            'specialization': specialization,
            'results': []
        })


class FacilityViewSet(viewsets.ModelViewSet):
    """
    ViewSet for health facility management.
    """
    permission_classes = [IsAuthenticated]
    queryset = User.objects.none()  # Placeholder until HealthFacility model is implemented
    # serializer_class = HealthFacilitySerializer
    
    @action(detail=False, methods=['get'])
    def by_location(self, request):
        """Get facilities by location."""
        location = request.query_params.get('location', '')
        return Response({
            'message': 'Facilities by location endpoint',
            'location': location,
            'results': []
        })


class PatientVisitViewSet(viewsets.ModelViewSet):
    """
    ViewSet for patient visit management.
    """
    permission_classes = [IsAuthenticated]
    queryset = User.objects.none()  # Placeholder until PatientVisit model is implemented
    # serializer_class = PatientVisitSerializer
    
    @action(detail=False, methods=['get'])
    def today(self, request):
        """Get today's visits."""
        return Response({
            'message': 'Today\'s visits endpoint',
            'results': []
        })


class HealthRecordViewSet(viewsets.ModelViewSet):
    """
    Provide CRUD operations for patient health records.

    Access is limited to authenticated clinical staff or superusers. Collections
    support filtering by patient, provider, facility, record type, and date
    ranges to keep browsing focused on relevant medical history.
    """

    permission_classes = [IsClinicalStaff]
    queryset = (
        HealthRecord.objects.select_related("patient", "facility", "attending_provider")
        .prefetch_related("medications", "laboratory_tests")
        .all()
    )
    serializer_class = HealthRecordSerializer
    filterset_class = HealthRecordFilter
    search_fields = [
        "patient__patient_id",
        "patient__first_name",
        "patient__last_name",
        "facility__name",
        "attending_provider__first_name",
        "attending_provider__last_name",
    ]
    ordering_fields = ["record_date", "created_at"]
    ordering = ["-record_date"]

    serializer_action_map = {
        "list": HealthRecordSerializer,
        "retrieve": HealthRecordDetailSerializer,
        "create": HealthRecordCreateSerializer,
        "update": HealthRecordCreateSerializer,
        "partial_update": HealthRecordCreateSerializer,
    }

    def get_serializer_class(self):
        """
        Return the serializer configured for the current action.
        """

        return self.serializer_action_map.get(self.action, self.serializer_class)

    @action(detail=False, methods=["get"], url_path="by-patient")
    def by_patient(self, request):
        """
        List health records for a patient identifier.

        This helper allows clinicians to quickly pull a patient's timeline by
        passing their external `patient_id` as a query parameter.
        """

        patient_identifier = request.query_params.get("patient_id")
        if not patient_identifier:
            return Response({"results": []})

        queryset = self.filter_queryset(
            self.get_queryset().filter(patient__patient_id=patient_identifier)
        )
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page or queryset, many=True)
        if page is not None:
            return self.get_paginated_response(serializer.data)
        return Response({"results": serializer.data})


@require_http_methods(["GET"])
def health_check(request):
    """Health check endpoint for API monitoring."""
    return JsonResponse({
        'status': 'healthy',
        'service': 'OpenCare-Africa API',
        'version': '1.0.0',
        'timestamp': '2024-01-01T00:00:00Z',
        'endpoints': {
            'patients': '/api/v1/patients/',
            'health_workers': '/api/v1/health-workers/',
            'facilities': '/api/v1/facilities/',
            'visits': '/api/v1/visits/',
            'records': '/api/v1/records/',
        }
    })


@require_http_methods(["GET"])
def api_stats(request):
    """Get API usage statistics."""
    return JsonResponse({
        'total_requests': 0,
        'active_users': 0,
        'popular_endpoints': [],
        'response_times': {
            'average': 0,
            'p95': 0,
            'p99': 0
        }
    })


@require_http_methods(["POST"])
def export_data(request):
    """Export data in various formats."""
    format_type = request.data.get('format', 'json')
    data_type = request.data.get('type', 'patients')
    
    return JsonResponse({
        'message': 'Data export endpoint',
        'format': format_type,
        'type': data_type,
        'download_url': None
    })
