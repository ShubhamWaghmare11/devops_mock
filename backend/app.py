from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend origin (adjust if your frontend runs somewhere else)
origins = [
    "http://localhost:3000",  # frontend URL
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # allows this origin to make requests
    allow_credentials=True,
    allow_methods=["*"],          # allow all HTTP methods (GET, POST, etc)
    allow_headers=["*"],          # allow all headers
)

@app.get("/api/hello")
def hello():
    return {"message": "Hello from Backend!"}
