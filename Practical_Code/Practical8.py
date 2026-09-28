# Import FastAPI
from fastapi import FastAPI

# Import BackgroundTasks
from fastapi import BackgroundTasks

# Used to simulate delay
import time

# Create FastAPI application
app = FastAPI()


# -------------------------------
# Background Task Function
# -------------------------------
def send_email(email: str):
    """
    This function simulates sending an email.   
    It runs in the background.
    """

    print(f"📧 Sending email to: {email}")

    # Simulate email sending delay
    time.sleep(10)

    print("✅ Email sent successfully!")


# -------------------------------
# API Endpoint
# -------------------------------
@app.post("/register")
async def register(email: str, background_tasks: BackgroundTasks):
    """
    Register a user and send a welcome email
    in the background.
    """

    print("👤 User registered successfully!")

    # Add background task
    background_tasks.add_task(send_email, email)

    return {
        "message": "Registration Successful!",
        "status": "Email will be sent in the background."
    }
