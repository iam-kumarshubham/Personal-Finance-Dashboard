# Personal Finance Dashboard

A full-stack web application for managing personal finances, tracking transactions, assets, and liabilities, and visualizing net worth over time.

## Tech Stack

### Backend
- **Python 3.11+**
- **FastAPI** - Modern, fast web framework for building APIs
- **SQLAlchemy** - SQL toolkit and ORM
- **PostgreSQL** - Database
- **Alembic** - Database migration tool
- **Pydantic** - Data validation using Python type annotations
- **JWT** - Authentication and authorization

### Frontend
- **React** - UI library
- **TypeScript** - Type-safe JavaScript
- **Tailwind CSS** - Utility-first CSS framework
- **Vite** - Build tool and development server
- **Axios** - HTTP client

## Features

### User Management
- User registration and authentication
- JWT-based authentication
- Protected routes and endpoints

### Transaction Management
- Add, edit, and delete transactions
- Categorize transactions (income/expense)
- Track transaction dates and descriptions
- Transaction summary and filtering

### Asset Management
- Track various types of assets
- Record asset values
- Asset categorization

### Liability Management
- Track debts and liabilities
- Record liability amounts
- Liability categorization

### Net Worth Tracking
- Real-time net worth calculation
- Historical net worth tracking
- Asset vs. Liability visualization

## Setup Instructions

### Prerequisites
- Python 3.11 or higher
- Node.js 16 or higher
- PostgreSQL 13 or higher
- Git

### Backend Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/iam-kumarshubham/Personal-Finance-Dashboard.git
   cd personal_finance_dashboard
```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On Unix or MacOS
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:

   Create a `.env` file in the root directory with the following variables:

   ```env
   DATABASE_URL=postgresql://user:password@localhost:5432/personal_finance
   SECRET_KEY=your-secret-key
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

5. Initialize the database:

   ```bash
   # Create database migrations
   alembic upgrade head
   ```

6. Run the backend server:

   ```bash
   uvicorn app.main:app --reload
   ```

### Frontend Setup

1. Navigate to the frontend directory:

   ```bash
   cd personal-finance-dashboard-frontend
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Set up environment variables:

   Create a `.env` file in the frontend directory:

   ```env
   VITE_API_URL=http://localhost:8000/api/v1
   ```

4. Run the development server:

   ```bash
   npm run dev
   ```

## API Documentation

Once the backend server is running, you can access the API documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Project Structure

```
personal_finance_dashboard/
├── alembic/                 # Database migrations
├── app/                    # Backend application
│   ├── api/               # API endpoints
│   ├── core/              # Core functionality
│   ├── crud/              # Database operations
│   ├── db/                # Database configuration
│   ├── models/            # SQLAlchemy models
│   ├── schemas/           # Pydantic models
│   └── utils/             # Utility functions
└── personal-finance-dashboard-frontend/  # Frontend application
    ├── src/
    │   ├── api/          # API client
    │   ├── components/   # React components
    │   ├── context/      # React context
    │   ├── hooks/        # Custom hooks
    │   ├── pages/        # Page components
    │   └── types/        # TypeScript types
    └── public/           # Static assets
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
