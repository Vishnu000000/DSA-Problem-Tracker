# DSA Problem Tracker

A full-stack web application to help you track your progress on Data Structures and Algorithms problems. This project was built to demonstrate proficiency in modern web development and DevOps practices.

![Screenshot of the DSA Problem Tracker application](https://placehold.co/800x400/E2E8F0/4A5568?text=Add+A+Project+Screenshot+Here)
*(Replace the placeholder above with a real screenshot of your running application!)*

---

## Features

- **Add Problems:** Easily add new problems with their name, URL, difficulty, and status.
- **View All Problems:** See your entire problem list in a clean, organized interface.
- **Update Status:** Track your progress from "To Do" to "Solving" to "Solved".
- **Delete Problems:** Remove problems you no longer want to track.
- **Responsive UI:** The interface is designed to work on both desktop and mobile devices.

---

## Tech Stack

This project is a demonstration of a modern, containerized web application architecture.

- **Backend:**
  - **Python 3.9**
  - **FastAPI:** A high-performance web framework for building APIs.
  - **Uvicorn:** An ASGI server to run the FastAPI application.
- **Frontend:**
  - **HTML5**
  - **Tailwind CSS:** A utility-first CSS framework for rapid UI development.
  - **Vanilla JavaScript:** For client-side logic and API communication.
- **DevOps:**
  - **Docker:** For containerizing the backend application, ensuring consistency across environments.
  - **GitHub Actions:** For setting up a CI/CD pipeline to automate building and publishing the Docker image (coming soon!).

---

## How to Run Locally

To run this project on your local machine, you'll need to have Python 3.7+ and Docker installed.

### 1. Running the Backend

First, let's get the FastAPI server running.

```bash
# Clone the repository
git clone [https://github.com/YOUR_USERNAME/dsa-problem-tracker.git](https://github.com/YOUR_USERNAME/dsa-problem-tracker.git)
cd dsa-problem-tracker

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload
```

The API will now be available at `http://localhost:8000`.

### 2. Running the Frontend

Simply open the `index.html` file in your web browser. It is configured to communicate with the backend server running on `localhost:8000`.

### 3. Running with Docker (Recommended)

The easiest way to run the backend is with Docker. This is how it would be run in a production-like environment.

```bash
# Make sure you are in the project's root directory

# Build the Docker image
docker build -t dsa-tracker-api .

# Run the Docker container
docker run -d -p 8000:8000 --name dsa-tracker-container dsa-tracker-api
```

The API will be running in a container, accessible at `http://localhost:8000`.

---

## Project Purpose

This project serves as a key portfolio piece, demonstrating a practical understanding of:

- **API Design:** Crafting a clean, well-documented RESTful API.
- **Full-Stack Development:** Integrating a frontend with a backend service.
- **Containerization:** Using Docker to package an application for reliable deployment.
- **Software Engineering Best Practices:** Writing clean, organized, and documented code.

