# Flask CI/CD Demo

A simple Flask application with complete CI/CD pipeline using GitHub Actions for automated deployment to AWS EC2.

## 🏗️ Project Structure

```
flask-cicd-demo/
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── templates/
│   └── index.html           # HTML template
├── tests/
│   └── test_app.py          # Unit tests
├── deploy/
│   ├── flask-app.service    # Systemd service file
│   └── setup-ec2.sh         # EC2 setup script
└── .github/
    └── workflows/
        └── ci-cd.yml        # GitHub Actions pipeline
```

## 🔄 CI/CD Pipeline

The pipeline automatically runs when code is pushed to the `main` branch:

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│    LINT     │───▶│    TEST     │───▶│    BUILD    │───▶│   DEPLOY    │
│             │    │             │    │             │    │   (EC2)     │
│ - Flake8    │    │ - Pytest    │    │ - Package   │    │ - SSH       │
│ - Style     │    │ - Coverage  │    │ - Artifact  │    │ - Restart   │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

### Pipeline Jobs:

1. **Lint** - Code quality check with Flake8
2. **Test** - Run pytest with coverage report
3. **Build** - Create deployment package
4. **Deploy** - Deploy to AWS EC2 via SSH

## 🚀 Setup Instructions

### 1. AWS EC2 Setup

1. Launch an EC2 instance (Ubuntu 22.04 recommended)
2. Configure Security Group:
   - SSH (port 22) - Your IP
   - HTTP (port 5000) - Anywhere (0.0.0.0/0)
3. SSH into EC2 and run setup script:
   ```bash
   chmod +x deploy/setup-ec2.sh
   ./deploy/setup-ec2.sh
   ```

### 2. GitHub Secrets Configuration

Add these secrets to your GitHub repository (`Settings > Secrets > Actions`):

| Secret Name    | Description                        |
|----------------|-----------------------------------|
| `EC2_HOST`     | EC2 Public IP or DNS              |
| `EC2_USER`     | SSH username (usually `ubuntu`)   |
| `EC2_SSH_KEY`  | Private SSH key (PEM file content)|

### 3. Push Code to Trigger Pipeline

```bash
git add .
git commit -m "Initial commit"
git push origin main
```

## 📋 API Endpoints

| Endpoint       | Method | Description          |
|---------------|--------|---------------------|
| `/`           | GET    | Home page           |
| `/api/health` | GET    | Health check        |
| `/api/info`   | GET    | App information     |

## 🧪 Run Tests Locally

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/ -v

# Run with coverage
pytest tests/ -v --cov=. --cov-report=term-missing
```

## 🏃 Run Application Locally

```bash
# Activate virtual environment
source venv/bin/activate

# Run Flask development server
python app.py

# Or with Gunicorn (production)
gunicorn --workers 3 --bind 0.0.0.0:5000 app:app
```

## 📝 License

MIT License
