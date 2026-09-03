from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError


app = FastAPI()


# ==========================================
# JWT SETTINGS
# ==========================================

SECRET_KEY = "mysecret"
ALGORITHM = "HS256"


# ==========================================
# USERS
# ==========================================

users = {

    "disha": {
        "password": "1904",
        "role": "student"
    },

    "nitish": {
        "password": "2201",
        "role": "teacher"
    }

}


# ==========================================
# OAUTH2 TOKEN
# ==========================================

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)


# ==========================================
# LOGIN API
# ==========================================

@app.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends()
):

    username = form_data.username
    password = form_data.password


    # Check whether user exists

    if username not in users:

        raise HTTPException(
            status_code=401,
            detail="User not found"
        )


    # Check password

    if users[username]["password"] != password:

        raise HTTPException(
            status_code=401,
            detail="Wrong password"
        )


    # Get user role

    role = users[username]["role"]


    # Create JWT token

    token_data = {
        "username": username,
        "role": role
    }


    token = jwt.encode(
        token_data,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


    return {

        "access_token": token,
        "token_type": "bearer"

    }


# ==========================================
# GET CURRENT USER
# ==========================================

def get_current_user(
    token: str = Depends(oauth2_scheme)
):

    try:

        # Decode JWT token

        data = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )


        username = data.get("username")
        role = data.get("role")


        # Check token data

        if username is None or role is None:

            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )


        return {
            "username": username,
            "role": role
        }


    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )


# ==========================================
# STUDENT API
# ==========================================

@app.get("/student")
def student_api(
    user = Depends(get_current_user)
):

    # Check role

    if user["role"] != "student":

        raise HTTPException(
            status_code=403,
            detail="Only students can access this API"
        )


    return {

        "message": "Welcome Student",

        "username": user["username"]

    }


# ==========================================
# TEACHER API
# ==========================================

@app.get("/teacher")
def teacher_api(
    user = Depends(get_current_user)
):

    # Check role

    if user["role"] != "teacher":

        raise HTTPException(
            status_code=403,
            detail="Only teachers can access this API"
        )


    return {

        "message": "Welcome Teacher",

        "username": user["username"]

    }
