# 🏥 Patient Management System API

A comprehensive RESTful API built with FastAPI for managing patient records with automatic BMI calculation and health assessment.

## 📋 Overview

The Patient Management System API provides a robust backend solution for healthcare applications to manage patient records efficiently. It features automatic BMI (Body Mass Index) calculation and health verdict assessment based on patient data, with full CRUD operations support.

## ✨ Key Features

- **Complete CRUD Operations**: Create, Read, Update, and Delete patient records
- **Automatic BMI Calculation**: Computes BMI automatically from height and weight
- **Health Assessment**: Provides health verdict (Underweight, Normal, Overweight, Obese)
- **Data Validation**: Robust input validation using Pydantic models
- **Sorting Capabilities**: Sort patients by height, weight, or BMI
- **JSON Data Persistence**: Simple file-based storage system
- **RESTful Design**: Clean and intuitive API endpoints
- **Interactive Documentation**: Auto-generated API docs with Swagger UI

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Patient_Appointment_system_API
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```

4. **Access the API**
   - API Base URL: `http://127.0.0.1:8000`
   - Interactive Docs: `http://127.0.0.1:8000/docs`
   - Alternative Docs: `http://127.0.0.1:8000/redoc`

## 📚 API Endpoints

### General Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/about` | API information |

### Patient Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/view` | Get all patients |
| GET | `/patient/{patient_id}` | Get specific patient details |
| POST | `/create` | Create new patient record |
| PUT | `/edit/{patient_id}` | Update patient information |
| DELETE | `/delete/{patient_id}` | Delete patient record |
| GET | `/sort` | Sort patients by criteria |

## 💡 Usage Examples

### Create a New Patient

```bash
POST /create
```

**Request Body:**
```json
{
  "id": "P001",
  "name": "John Doe",
  "city": "New York",
  "age": 30,
  "gender": "male",
  "height": 1.75,
  "weight": 70.0
}
```

**Response:**
```json
{
  "message": "patient created successfully"
}
```

*Note: BMI and health verdict are automatically calculated*

### Get Patient Details

```bash
GET /patient/P001
```

**Response:**
```json
{
  "name": "John Doe",
  "city": "New York",
  "age": 30,
  "gender": "male",
  "height": 1.75,
  "weight": 70.0,
  "bmi": 22.86,
  "verdict": "Normal"
}
```

### Update Patient Information

```bash
PUT /edit/P001
```

**Request Body:**
```json
{
  "weight": 75.0,
  "city": "Los Angeles"
}
```

*Note: BMI and verdict are recalculated automatically*

### Sort Patients

```bash
GET /sort?sort_by=bmi&order=desc
```

**Query Parameters:**
- `sort_by`: `height`, `weight`, or `bmi`
- `order`: `asc` or `desc`

### Delete Patient

```bash
DELETE /delete/P001
```

## 📊 Data Model

### Patient Schema

| Field | Type | Description | Validation |
|-------|------|-------------|------------|
| id | string | Unique patient identifier | Required |
| name | string | Patient's full name | Required |
| city | string | Patient's city | Required |
| age | integer | Patient's age | 0 < age < 120 |
| gender | string | Patient's gender | male/female/others |
| height | float | Height in meters | > 0 |
| weight | float | Weight in kilograms | > 0 |
| bmi | float | Body Mass Index | Auto-calculated |
| verdict | string | Health assessment | Auto-calculated |

### Health Verdict Categories

- **Underweight**: BMI < 18.5
- **Normal**: 18.5 ≤ BMI < 25
- **Overweight**: BMI ≥ 25

## 🛠️ Technology Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **Pydantic**: Data validation using Python type annotations
- **Uvicorn**: Lightning-fast ASGI server
- **Python 3.7+**: Core programming language

## 📁 Project Structure

```
Patient_Appointment_system_API/
│
├── main.py              # Main application file with API endpoints
├── patients.json        # JSON database for patient records
├── requirements.txt     # Project dependencies
└── README.md           # Project documentation
```

## 🔒 Error Handling

The API includes comprehensive error handling:

- **400 Bad Request**: Invalid input or duplicate patient ID
- **404 Not Found**: Patient ID doesn't exist
- **422 Unprocessable Entity**: Validation errors

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Built with ❤️ using FastAPI

## 🐛 Known Issues

- Data is stored in a JSON file (consider migrating to a proper database for production)
- No authentication/authorization implemented
- No pagination for large datasets

## 🚧 Future Enhancements

- [ ] Add database integration (PostgreSQL/MongoDB)
- [ ] Implement user authentication and authorization
- [ ] Add appointment scheduling features
- [ ] Include medical history tracking
- [ ] Add pagination for large datasets
- [ ] Implement search functionality
- [ ] Add email notifications
- [ ] Create a frontend dashboard

## 📞 Support

For support, please open an issue in the GitHub repository.

---

**Note**: This is a demonstration project. For production use, consider implementing proper database storage, authentication, and security measures.
