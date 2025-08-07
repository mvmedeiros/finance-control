# 💸 Finance Control App

A full-stack personal finance management platform built with:

- 🧠 **Django + Django REST Framework** (Backend API)
- 💻 **React.js** (Frontend SPA)

It allows users to track incomes, expenses, transfers, manage accounts, and create reports based on the history — all with a clean, responsive interface.


## 🚧 Development Progress

### 🧠 Backend (Django)
- [ ] Create models: `Transaction`, `Category`, `Account`, `User`
- [ ] Initial data migration for default categories and transaction types
- [ ] Handle dynamic creation of categories via serializer
- [ ] Handle dynamic creation of users via serializer
- [ ] Handle dynamic creation of transaction via serializer
- [ ] API endpoints for transaction CRUD
- [ ] Add filtering by date/category/account/user/transaction type
- [ ] Account balance calculation with future projections
- [ ] Transaction summary/report endpoints
- [ ] Swagger/OpenAPI documentation

### 💻 Frontend (React)
- [ ] Create base components and pages
- [ ] Form to create new transaction
- [ ] Form to create new categories
- [ ] Form to create new accounts
- [ ] Form to create new users
- [ ] Account and category management views
- [ ] Display transactions list, filtering by user, categories, types, and flags
- [ ] Filters and reports
- [ ] Charts and dashboard UI
---

## 🧱 Project Structure
finance-control/
├── backend/ # Django project
│ ├── users/ # Custom user model & auth
│ ├── accounts/ # Bank accounts
│ ├── categories/ # Income/expense/transfer categories
│ ├── transactions/ # Transaction logic
│ ├── api/ # DRF routers, views (optional)
│ └── manage.py
├── frontend/ # React app
│ └── src/
│ └── components/
│ └── pages/
│ └── services/ # API calls to Django backend
│ └── package.json

---

## ⚙️ Setup Instructions

### 🐍 Backend (Django)

1. Create virtual environment & install dependencies:

cd backend
python -m venv venv
.venv/scripts/activate
pip install -r requirements.txt

2. Run migrations and create superuser:

python manage.py migrate
python manage.py createsuperuser


3. Start the backend server:

python manage.py runserver

Backend runs at: http://localhost:8000/

---

## ⚛️ Frontend (React)

1. Install dependencies:

cd frontend
npm install

2. Start the React development server:

npm run dev  # or: npm start

Frontend runs at: http://localhost:3000/

---

## 🔄 API Overview (Key Endpoints)

| Endpoint             | Method   | Description                  |
| -------------------- | -------- | ---------------------------- |
| xxxxx | xxx | xxx |
| xxxxx | xxx | xxx |

---
