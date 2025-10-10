"""
Serializers for patient health record APIs.
"""

from __future__ import annotations

from rest_framework import serializers

from apps.core.models import User
from apps.patients.models import Patient

from .models import HealthRecord


class HealthRecordSerializer(serializers.ModelSerializer):
    """
    Lightweight representation of a health record for list views.
    """

    patient_name = serializers.CharField(source="patient.get_full_name", read_only=True)
    facility_name = serializers.CharField(source="facility.name", read_only=True)
    provider_name = serializers.CharField(
        source="attending_provider.get_full_name", read_only=True
    )

    class Meta:
        model = HealthRecord
        fields = [
            "id",
            "patient",
            "patient_name",
            "facility",
            "facility_name",
            "record_type",
            "record_date",
            "attending_provider",
            "provider_name",
            "assessment",
            "is_confidential",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class HealthRecordDetailSerializer(HealthRecordSerializer):
    """
    Extend the base health record serializer with full clinical context.
    """

    class Meta(HealthRecordSerializer.Meta):
        fields = HealthRecordSerializer.Meta.fields + [
            "chief_complaint",
            "history_of_present_illness",
            "past_medical_history",
            "family_history",
            "social_history",
            "vital_signs",
            "physical_examination",
            "diagnosis",
            "treatment_plan",
            "follow_up_plan",
            "notes",
            "attachments",
        ]


class HealthRecordCreateSerializer(serializers.ModelSerializer):
    """
    Handle creation and updates while validating related foreign keys.
    """

    class Meta:
        model = HealthRecord
        fields = [
            "patient",
            "facility",
            "record_type",
            "record_date",
            "attending_provider",
            "chief_complaint",
            "history_of_present_illness",
            "past_medical_history",
            "family_history",
            "social_history",
            "vital_signs",
            "physical_examination",
            "assessment",
            "diagnosis",
            "treatment_plan",
            "follow_up_plan",
            "notes",
            "attachments",
            "is_confidential",
            "is_active",
        ]

    def validate(self, attrs):
        """
        Ensure the referenced patient, provider, and facility are active entries.
        """

        patient: Patient = attrs.get("patient")
        provider: User | None = attrs.get("attending_provider")
        if patient and not patient.is_active:
            raise serializers.ValidationError("Patient profile is inactive.")

        if provider and not provider.is_active:
            raise serializers.ValidationError("Attending provider account is inactive.")

        return attrs
