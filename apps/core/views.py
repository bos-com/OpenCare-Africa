"""
Core views for OpenCare-Africa health system.
"""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    """Home page view."""
    context = {
        'title': 'OpenCare-Africa - Health Informatics Platform',
        'description': 'Empowering health systems across Africa with innovative technology solutions.',
    }
    return render(request, 'core/home.html', context)


@login_required
def dashboard(request):
    """Dashboard view for authenticated users."""
    context = {
        'title': 'Dashboard - OpenCare-Africa',
        'user': request.user,
    }
    return render(request, 'core/dashboard.html', context)


def about(request):
    """About page view."""
    context = {
        'title': 'About - OpenCare-Africa',
        'description': 'Learn more about our mission to improve healthcare in Africa.',
    }
    return render(request, 'core/about.html', context)


def contact(request):
    """Contact page view."""
    context = {
        'title': 'Contact - OpenCare-Africa',
        'description': 'Get in touch with our team.',
    }
    return render(request, 'core/contact.html', context)


@require_http_methods(["GET"])
def health_check(request):
    """Health check endpoint for monitoring."""
    return JsonResponse({
        'status': 'healthy',
        'service': 'OpenCare-Africa',
        'version': '1.0.0',
        'timestamp': '2024-01-01T00:00:00Z'
    })


class HealthMetricsView(LoginRequiredMixin, View):
    """View for displaying health system metrics."""
    
    def get(self, request):
        """Get health metrics data."""
        # This would typically fetch data from various models
        metrics = {
            'total_patients': 0,  # Patient.objects.count()
            'total_health_workers': 0,  # User.objects.filter(user_type__in=['doctor', 'nurse', 'midwife']).count()
            'total_facilities': 0,  # HealthFacility.objects.count()
            'active_visits': 0,  # PatientVisit.objects.filter(status='in_progress').count()
        }
        
        context = {
            'title': 'Health Metrics - OpenCare-Africa',
            'metrics': metrics,
        }
        return render(request, 'core/health_metrics.html', context)


class SystemStatusView(LoginRequiredMixin, View):
    """View for displaying system status."""
    
    def get(self, request):
        """Get system status information."""
        # This would typically check various system components
        system_status = {
            'database': 'healthy',
            'cache': 'healthy',
            'celery': 'healthy',
            'external_apis': 'healthy',
        }
        
        context = {
            'title': 'System Status - OpenCare-Africa',
            'system_status': system_status,
        }
        return render(request, 'core/system_status.html', context)
