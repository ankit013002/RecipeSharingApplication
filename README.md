# 🍽️ Recipe Sharing Application

A web application that allows users to share and explore recipes, built using **Flask (backend)** and **Vite + React (frontend)**.

## 🚀 Getting Started
Follow these steps to set up the project on your local machine.

### **Prerequisites**
Ensure you have the following installed:
- **Python** (≥3.8) - [Download](https://www.python.org/downloads/)
- **Node.js** (≥16.0) - [Download](https://nodejs.org/)
- **npm** (comes with Node.js)

---

## 🛠 Backend Setup (Flask)
### **1. Create a Virtual Environment (Recommended)**
```bash
python -m venv venv
```
### **2. Activate the Virtual Environment**
#### **Windows:**
```bash
venv\Scripts\activate
```
#### **Mac/Linux:**
```bash
source venv/bin/activate
```
### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```
### **4. Navigate to the Backend Directory**
```bash
cd backend
```
### **5. Run the Backend Server**
```bash
python app.py
```
Your Flask API should now be running at [http://127.0.0.1:5000/](http://127.0.0.1:5000/) 🎉

---

## 🎨 Frontend Setup (Vite + React)
### **1. Navigate to the Frontend Directory**
```bash
cd frontend
```
### **2. Install Dependencies**
```bash
npm install
```
### **3. Start the Development Server**
```bash
npm run dev
```
The frontend should now be running at [http://localhost:5173/](http://localhost:5173/) 🎉

---

## 🔗 Connecting Frontend & Backend
To allow the frontend to communicate with the backend:

- Ensure Flask is running at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
- Ensure CORS is enabled in Flask
- If not already done, install `flask-cors` and modify `app.py`:
- If everything is set up correctly, visiting the React app should display:
     ```plaintext
     Recipe Sharing Application
     Backend Message: Recipe Sharing App Backend
     ```

---

## 💡 Features (Planned)
✔️ Users can upload recipes  
✔️ Users can browse and search for recipes  
✔️ Recipe ratings and reviews  
✔️ User authentication (login/signup)  

---

## 🐞 Troubleshooting
### **Frontend Issues**
#### **Error: 'vite' is not recognized**
➜ Run:
```bash
npm install
```
Then retry:
```bash
npm run dev
```

### **Backend Issues**
#### **ModuleNotFoundError (e.g., Flask not found)**
➜ Ensure you're in the virtual environment:
```bash
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```
Then install dependencies:
```bash
pip install -r requirements.txt
```

---

## 📜 Contributors
- **Ankit Patel**  
- **Dhairya Amin**  
- **Michael Allen**  

---
