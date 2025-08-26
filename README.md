# OpenCare-Africa Backend

A comprehensive health informatics platform backend built with Django, designed specifically for healthcare management in Africa.

## 🏥 Project Overview

OpenCare-Africa is a robust, scalable backend system for managing healthcare operations, patient records, health worker management, and health facility operations. The system is built with modern Django practices and includes comprehensive API endpoints for integration with frontend applications.

## ✨ Features

### Core Functionality
- **User Management**: Comprehensive user roles and permissions for healthcare workers
- **Patient Management**: Complete patient lifecycle management with medical history
- **Health Facility Management**: Facility operations, services, and resource management
- **Health Records**: Comprehensive medical records with FHIR compliance
- **Analytics & Reporting**: Health metrics, disease outbreak tracking, and performance analytics
- **API-First Design**: RESTful API with OpenAPI/Swagger documentation

### Technical Features
- **Django 4.2+**: Modern Django with best practices
- **PostgreSQL**: Robust database with healthcare-optimized schemas
- **Redis**: Caching and session management
- **Celery**: Background task processing
- **Docker**: Containerized deployment
- **JWT Authentication**: Secure API authentication
- **Health Checks**: System monitoring and diagnostics

## 🏗️ Architecture

```
OpenCare-Africa/
├── apps/                    # Django applications
│   ├── core/               # Core models and utilities
│   ├── patients/           # Patient management
│   ├── health_workers/     # Healthcare personnel management
│   ├── facilities/         # Health facility operations
│   ├── records/            # Medical records management
│   ├── analytics/          # Health analytics and reporting
│   └── api/                # API endpoints and viewsets
├── config/                 # Project configuration
│   ├── settings/           # Environment-specific settings
│   ├── urls.py            # Main URL configuration
│   └── celery.py          # Celery configuration
├── templates/              # HTML templates
├── static/                 # Static files
├── media/                  # User-uploaded files
├── docs/                   # Documentation
└── scripts/                # Database and deployment scripts
```

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- PostgreSQL 15+
- Redis 7+
- Docker & Docker Compose (optional)

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/bos-com/OpenCare-Africa.git
   cd opencare-africa
   ```

2. **Set up environment variables**
   ```bash
   cp env.example .env
   # Edit .env with your configuration
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**
   ```bash
   # Create PostgreSQL database
   createdb opencare_africa
   
   # Run migrations
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

### Docker Setup

1. **Start all services**
   ```bash
   docker-compose up -d
   ```

2. **Run migrations**
   ```bash
   docker-compose exec web python manage.py migrate
   ```

3. **Create superuser**
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

4. **Access the application**
   - Web: http://localhost:8000
   - Admin: http://localhost:8000/admin
   - API Docs: http://localhost:8000/api/docs/

## 📊 API Documentation

The API is fully documented using OpenAPI/Swagger:

- **Swagger UI**: `/api/docs/`
- **ReDoc**: `/api/redoc/`
- **OpenAPI Schema**: `/api/schema/`

### Key API Endpoints

- **Authentication**: `/api/v1/auth/`
- **Patients**: `/api/v1/patients/`
- **Health Workers**: `/api/v1/health-workers/`
- **Facilities**: `/api/v1/facilities/`
- **Health Records**: `/api/v1/records/`
- **Analytics**: `/api/v1/analytics/`

## 🗄️ Database Schema

### Core Models
- **User**: Extended user model with healthcare worker profiles
- **Location**: Hierarchical geographic location management
- **HealthFacility**: Health facility information and services
- **AuditTrail**: Comprehensive audit logging

### Patient Models
- **Patient**: Complete patient information and demographics
- **PatientVisit**: Patient visit tracking and scheduling
- **PatientMedicalHistory**: Medical history and conditions

### Healthcare Models
- **HealthWorkerProfile**: Extended healthcare worker profiles
- **ProfessionalQualification**: Qualifications and certifications
- **WorkSchedule**: Work schedules and availability
- **PerformanceEvaluation**: Performance tracking and reviews

### Facility Models
- **FacilityService**: Services offered by health facilities
- **FacilityStaff**: Staff management and assignments
- **FacilityEquipment**: Medical equipment tracking
- **FacilityInventory**: Medical supplies and inventory

### Records Models
- **HealthRecord**: Comprehensive medical records
- **VitalSigns**: Patient vital signs and measurements
- **Medication**: Prescription and medication management
- **LaboratoryTest**: Lab test results and interpretation
- **ImagingStudy**: Medical imaging results

### Analytics Models
- **HealthMetrics**: Health KPIs and metrics
- **DiseaseOutbreak**: Disease outbreak tracking
- **HealthReport**: Automated health reports
- **PatientAnalytics**: Patient-specific analytics

## 🔧 Configuration

### Environment Variables

```bash
# Django Configuration
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration
DB_ENGINE=django.db.backends.postgresql
DB_NAME=opencare_africa
DB_USER=opencare_user
DB_PASSWORD=opencare_password
DB_HOST=localhost
DB_PORT=5432

# Redis Configuration
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0

# JWT Configuration
JWT_ACCESS_TOKEN_LIFETIME=5
JWT_REFRESH_TOKEN_LIFETIME=1
```

### Settings Files

- `config/settings/base.py`: Base configuration
- `config/settings/development.py`: Development environment
- `config/settings/production.py`: Production environment
- `config/settings/test.py`: Testing environment

## 🧪 Testing

```bash
# Run all tests
python manage.py test

# Run tests with coverage
coverage run --source='.' manage.py test
coverage report
coverage html

# Run specific app tests
python manage.py test apps.patients
python manage.py test apps.core
```

## 📈 Performance & Monitoring

### Health Checks
- Database connectivity
- Redis connectivity
- Storage availability
- System resources

### Monitoring
- Django Debug Toolbar (development)
- Sentry integration (production)
- Custom health metrics
- Performance analytics

### Caching
- Redis-based caching
- Database query optimization
- Static file caching
- API response caching

## 🚀 Deployment

### Production Checklist
- [ ] Set `DEBUG=False`
- [ ] Configure production database
- [ ] Set up SSL/TLS certificates
- [ ] Configure static file serving
- [ ] Set up monitoring and logging
- [ ] Configure backup strategies
- [ ] Set up CI/CD pipelines

### Docker Production
```bash
# Build production image
docker build -t opencare-africa:latest .

# Run with production settings
docker run -e DJANGO_SETTINGS_MODULE=config.settings.production opencare-africa:latest
```

## 🔒 Security Features

- JWT-based authentication
- Role-based access control
- Comprehensive audit logging
- Input validation and sanitization
- CORS configuration
- Rate limiting (configurable)
- Secure password policies

## 📚 Documentation

- **API Documentation**: Built-in Swagger/OpenAPI docs
- **Code Documentation**: Comprehensive docstrings
- **Admin Interface**: Django admin for data management
- **User Guides**: Available in `/docs/` directory

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

### Development Guidelines
- Follow PEP 8 style guidelines
- Write comprehensive docstrings
- Include tests for new features
- Update documentation as needed
- Use meaningful commit messages

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Documentation**: Check the `/docs/` directory
- **Issues**: Report bugs via GitHub Issues
- **Discussions**: Use GitHub Discussions for questions
- **Email**: Contact the development team

## 🗺️ Roadmap

### Phase 1 (Current)
- ✅ Core backend infrastructure
- ✅ Patient management system
- ✅ Health worker management
- ✅ Facility management
- ✅ Basic API endpoints

### Phase 2 (Next)
- 🔄 Advanced analytics dashboard
- 🔄 Mobile API optimization
- 🔄 Integration with external systems
- 🔄 Advanced reporting features

### Phase 3 (Future)
- 📋 AI-powered health insights
- 📋 Telemedicine integration
- 📋 Advanced data visualization
- 📋 Multi-language support

## 🙏 Acknowledgments

- Django community for the excellent framework
- Healthcare professionals for domain expertise
- Open source contributors for various packages
- African healthcare workers for inspiration

---

**OpenCare-Africa** - Empowering healthcare in Africa through technology.
