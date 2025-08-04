from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, HttpUrl
from typing import List

# Create the FastAPI app instance
app = FastAPI(
    title="DSA Problem Tracker API",
    description="An API to track DSA problems for your portfolio project.",
    version="1.0.0",
)

# --- CORS Middleware ---
# This allows your frontend (running on a different origin) to communicate
# with this backend. In a real production environment, you would restrict
# this to your specific frontend's domain.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


# --- Pydantic Data Models ---
# These models define the structure of the data your API will handle.
# Pydantic automatically handles data validation.

class ProblemBase(BaseModel):
    name: str
    url: HttpUrl
    difficulty: str
    status: str

class ProblemCreate(ProblemBase):
    pass

class Problem(ProblemBase):
    id: int

# --- In-Memory Database ---
# A simple list to store problems. This avoids needing a full database setup,
# which is perfect for a quick portfolio project. The data will reset if the
# server restarts.
db: List[Problem] = [
    Problem(id=1, name="Two Sum", url="https://leetcode.com/problems/two-sum/", difficulty="Easy", status="Solved"),
    Problem(id=2, name="Add Two Numbers", url="https://leetcode.com/problems/add-two-numbers/", difficulty="Medium", status="Solving"),
    Problem(id=3, name="Longest Substring Without Repeating Characters", url="https://leetcode.com/problems/longest-substring-without-repeating-characters/", difficulty="Medium", status="To Do"),
]
# Keep track of the next available ID
next_id = 4


# --- API Endpoints ---

@app.get("/", tags=["Root"])
def read_root():
    """A simple root endpoint to confirm the API is running."""
    return {"message": "Welcome to the DSA Problem Tracker API!"}

@app.get("/problems", response_model=List[Problem], tags=["Problems"])
def get_all_problems():
    """Retrieve all problems from the database."""
    return db

@app.post("/problems", response_model=Problem, status_code=201, tags=["Problems"])
def create_problem(problem: ProblemCreate):
    """Create a new problem and add it to the database."""
    global next_id
    new_problem = Problem(id=next_id, **problem.dict())
    db.append(new_problem)
    next_id += 1
    return new_problem

@app.get("/problems/{problem_id}", response_model=Problem, tags=["Problems"])
def get_problem_by_id(problem_id: int):
    """Retrieve a single problem by its ID."""
    for p in db:
        if p.id == problem_id:
            return p
    raise HTTPException(status_code=404, detail="Problem not found")

@app.delete("/problems/{problem_id}", status_code=204, tags=["Problems"])
def delete_problem(problem_id: int):
    """Delete a problem from the database by its ID."""
    global db
    problem_to_delete = None
    for p in db:
        if p.id == problem_id:
            problem_to_delete = p
            break
    
    if not problem_to_delete:
        raise HTTPException(status_code=404, detail="Problem not found")
        
    db.remove(problem_to_delete)
    return
