# 🚀 CRUD Assignment – Backend & Frontend

## 🧩 Task 1: Backend – CRUD APIs (Flask)

✅ Create, Read, Update, Delete **Comments** for a given Task
✅ RESTful API design
✅ Automated tests included

### 🔧 Tech Stack

* 🐍 Python (Flask)
* 🧪 Pytest
* 🗄️ SQLite / SQLAlchemy

### ▶️ Run Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\\Scripts\\activate
pip install -r requirements.txt
flask run
```

### 🧪 Run Tests

```bash
python test_crud_operations.py
```

---

## 🎨 Task 2: Frontend – CRUD UI (React)

✅ UI to Create, View, Update, Delete **Tasks**
✅ Uses existing backend CRUD APIs
✅ Clean and simple UI

### 🔧 Tech Stack

* ⚛️ React
* 🌐 Axios
* 🎨 Basic CSS

### ▶️ Run Frontend

```bash
cd frontend
npm install
npm start
```

App will run at 👉 `http://localhost:3000`

---

## 📁 Project Structure

```
backend/    # Flask APIs + Tests
frontend/   # React UI
```

---

## 📌 Notes

* PRs are created from a **fork**, as per instructions
* CI workflow adjusted to support fork-based PRs
* Reasonable assumptions are documented in PRs

---

⭐ Thank you for reviewing my submission!

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Flask React Template

Boilerplate project for Flask, React & MongoDB based projects. This README documents the steps necessary to get the application up and running, and various components of the application.

| Build Status                                                                                                                                                                                                                                     | Code Coverage                                                                                                                                                                                                                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [![Production Deploy](https://github.com/jalantechnologies/flask-react-template/actions/workflows/production.yml/badge.svg?branch=main)](https://github.com/jalantechnologies/flask-react-template/actions/workflows/production.yml) | [![Code Coverage](https://sonarqube.platform.bettrhq.com/api/project_badges/measure?project=jalantechnologies_flask-react-template&metric=coverage&token=a4dd71c68afbb8da4b7ed1026329bf0933298f79)](https://sonarqube.platform.bettrhq.com/dashboard?id=jalantechnologies_flask-react-template) |

### Environments & URLs
This project has three deployment environments that everyone can access:

- **Production**
  - The live app for end users.
  - Web App URL: [https://flask-react-template.platform.bettrhq.com](https://flask-react-template.platform.bettrhq.com)
  - Temporal Workers Dashboard: [https://workers-dashboard.flask-react-template.platform.bettrhq.com/](https://workers-dashboard.flask-react-template.platform.bettrhq.com/)

- **Preview (per PR)**
  - A temporary environment for testing the latest changes in each PR
  - A unique URL is generated for every pull request (e.g. `https://<github_sha>.preview.platform.bettrhq.com`).
  - A dedicated temporal workers dashboard is also available at `https://<github_sha>.workers-dashboard.preview.platform.bettrhq.com/`

- **Permanent Preview**
  - Always reflects the latest `main` branch.
  - Useful for ongoing testing of the integrated codebase.
  - URL: [https://preview.flask-react-template.platform.bettrhq.com](https://preview.flask-react-template.platform.bettrhq.com)
  - Temporal Workers Dashboard: [https://preview.workers-dashboard.flask-react-template.platform.bettrhq.com](https://preview.workers-dashboard.flask-react-template.platform.bettrhq.com)

## Documentation Directory

- [Getting Started](docs/getting-started.md)
- [Backend Architecture](docs/backend-architecture.md)
- [Frontend Architecture](docs/frontend-architecture.md)
- [Logging](docs/logging.md)
- [Configuration](docs/configuration.md)
- [Secrets](docs/secrets.md)
- [Bootstrapping](docs/bootstrapping.md)
- [Scripts](docs/scripts.md)
- [Code Formatting](docs/code-formatting.md)
- [Workers](docs/workers.md)
- [CI/CD](docs/deployment.md)
- [Running Scripts in Production](docs/running-scripts-in-production.md)

## Best Practices

Once you have familiarized yourself with the documentation, head over to the [Engineering Handbook](https://github.com/jalantechnologies/handbook/blob/main/engineering/index.md) to learn about the best practices we follow at Better Software.

PS: Before you start working on the application, these [three git settings](https://spin.atomicobject.com/git-configurations-default/) are a must-have!

