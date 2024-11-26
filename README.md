# **EstateSphere-project: Real Estate Listing System**

## **Overview**
This is a web-based real estate management system built using the Django Framework and PostgreSQL. The project includes public and private sections, role-based access control, and an admin panel with custom functionalities.

---

## **Features**

### **Public Section** (Accessible to All Users)
- View property listings with pagination.
- Search properties based on location.

### **Private Section** (Accessible to Authenticated Users)
- Add properties to favorites.
- Access detailed information about each property.
- Favourite properties.
- Leave reviews on properties.
- Manage user profiles (update personal information).

### **Admin Panel**
- Manage users, properties, feedback, and favorites.
- Role-based permissions:
  - **Superusers**: Full CRUD permissions.
  - **Staff Users**: Limited permissions for data management.
- Enhanced admin functionality (custom filters, ordering, etc.).

### **Additional Features**
- Data Validation & Exception Handling to prevent crashes.
- Responsive Design.
- Authentication System: Register/Login/Logout functionality.

---

## **Tech Stack**
- **Backend:** Django Framework  
- **Database:** PostgreSQL  
- **Frontend:** Custom CSS and Bootstrap   

---

## **Installation**

Follow these steps to set up the project locally:

### **Prerequisites**
- Python (version 3.8 or higher)
- PostgreSQL installed and configured
- Virtual environment (optional but recommended)

### **Steps to Install**
1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies:
 - pip install -r requirements.txt
4. Create a .env file for environment variables:
  - DATABASE_NAME=YOUR_DB_NAME
  - DATABASE_USER=YOUR_DB_USER
  - DATABASE_PASSWORD=YOUR_DB_PASSWORD
  - DATABASE_HOST=HOST
  - DATABASE_PORT=PORT
5. Set up the database
6. Run migrations:
  - python manage.py makemigrations
  - python manage.py migrate
7. Run the development server:
  - python manage.py runserver

---

## **Future Enhancements**

1. Add filters for advanced property searches (e.g., price range, property type).
2. Enable image carousel for property details.
3. Integrate a payment gateway for property bookings.
4. Add an API for mobile app integration.
5. Many more!!!
