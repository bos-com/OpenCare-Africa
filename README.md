# BOSC Health Informatics Project

## Overview

Welcome to the Health Informatics project by the Bugema Open Source Community (BOSC). We develop open-source, data-driven health solutions to strengthen health systems, support mobile health (mHealth), ensure interoperability, and enable predictive analytics for communities in Uganda and beyond.

## Project Goals

- Track patient data securely.
- Support mobile health apps for community health workers and patients.
- Ensure interoperability with health standards.
- Provide health dashboards and AI-driven insights (e.g., malaria risk).

## Tech Stack

| **Purpose**            | **Framework/Tool**                     | **Why We Use It**                                                                 |
|------------------------|---------------------------------------|----------------------------------------------------------------------------------|
| Health Data Standards | DHIS2, FHIR                            | Widely used for health records and reporting.                                   |
| Backend/API           | Django REST Framework, Node.js        | Flexible REST APIs for health systems.                                           |
| Data Visualization    | Metabase, Superset, Power BI Embedded | Analytics and reporting for health data.                                        |
| Mobile App            | React Native                          | mHealth apps for community health workers and patients.                         |
| Interoperability      | OpenHIM                              | Integrates data across health systems.                                          |
| AI/ML Tools           | TensorFlow, scikit-learn, Streamlit   | Predictive modeling for health trends.                                          |

**Cross-Cutting Tools**:
- **GitHub Actions**: CI/CD automation.
- **Docker**: Consistent environments.
- **Firebase/Supabase**: Authentication and database.
- **i18n Libraries**: Local language support.

## Setup Instructions

### Prerequisites
- **Git**: For version control.
- **Python 3.8+**: For Django/Streamlit.
- **Node.js**: For Node.js backend
- **Docker**: For containerized setups.
- **MongoDB**: For data storage.
- **API Keys**: For OpenHIM.

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/BOSC-Bugema/health-informatics.git
   cd health-informatics
   ```

2. **Set Up Environment**:
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Update with API keys (e.g., Firebase) and database credentials.

3. **Choose Your Setup**:
   - **Django Backend**:
     ```bash
     pip install -r requirements.txt
     python manage.py migrate
     python manage.py runserver
     ```
   - **Node.js Backend**:
     ```bash
     npm install
     npm run dev
     ```
   - **Streamlit for AI/ML**:
     ```bash
     pip install -r requirements.txt
     streamlit run app.py
     ```

4. **Docker Setup (Alternative and recommendendaed)**:
   ```bash
   docker-compose up --build
   ```

5. **Configure DHIS2**:
   - Follow  `docs/dhis2_setup.md` for health data standards.

### Running the Project

- **Backend**: `python manage.py runserver` (Django) or `npm run dev` (Node.js).
- **Mobile App**: `flutter run` or `npx react-native run-android`.
- **Dashboards**: Run Metabase/Superset via Docker (see `docs/dashboard_setup.md`).
- **AI/ML**: Access Streamlit at `http://localhost:8008`.

### Testing

- Run tests: `pytest` (Python) or `npm test` (Node.js).
- Check GitHub Actions for CI/CD pipelines.

## GitHub Configuration

We follow BOSC’s standards for secure and collaborative development:

- **Security**:
  - Code Scanning: Enabled via GitHub Advanced Security.
  - Secret Scanning: Detects credentials.
  - Dependency Review: Blocks vulnerable dependencies.
  - Branch Protection: Requires reviews and CI checks.
  - Audit Logs: Tracks activity.

- **Workflows**:
  - Template Repositories: Standardizes setups.
  - GitHub Actions: Automates CI/CD.
  - GitHub Packages: Stores private packages.
  - Collaboration: Uses commit conventions and PR templates.

- **Onboarding**:

  - See `docs/onboarding.md` for guides.
  - Join workshops for hands-on learning.
  - Use training repos for practice.

- **Monitoring**:
  - Track usage and audit logs.
  - Contact support via `SUPPORT.md`.

## Contribution Guidelines

- Use commit conventions (e.g., `feat: add patient tracking`).
- Follow PR templates and require one approval.
- Optimize for low-bandwidth and offline-first designs.
- Support local languages with i18n.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

Join us at [https://github.com/BOSC-Bugema](https://github.com/BOSC-Bugema) or email [kmuwanga@bugemauniv.ac.ug](mailto:kmuwanga@bugemauniv.ac.ug).

Let’s empower health systems together! 🩺 #OpenSource #HealthInformatics #BOSC
