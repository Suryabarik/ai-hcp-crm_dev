from fastapi import FastAPI
from routers import interaction_router, hcp_router
from dotenv import load_dotenv
import os

# ✅ Load environment variables
load_dotenv()

# ✅ Import DB Base and engine
from database.db import Base, engine

# ✅ Import all models so that they are registered with Base
import models.hcp
import models.interaction

# Create database tables automatically if they do not exist
print("Creating database tables if they do not exist...")
Base.metadata.create_all(bind=engine)
print("Tables created successfully!")

# Initialize FastAPI
app = FastAPI(title="AI HCP CRM")

# Include routers
app.include_router(interaction_router.router)
app.include_router(hcp_router.router)

# Root endpoint
@app.get("/")
def root():
    return {"message": "AI HCP CRM Backend is running"}
