# python -m pip install python-jose
# python -m pip install python-multipart
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt


app = FastAPI()


# =====================================
# SETTINGS
# =====================================

SECRET_KEY = "mysecret"
ALGORITHM = "HS256"


# =====================================
# SIMPLE USER
# =====================================

USERNAME = "nitish"
PASSWORD = "2113"


# =====================================
# OAUTH2
# =====================================

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)


# =====================================
# LOGIN
# =====================================

@app.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends()
):

    # Check username and password

    if (
        form_data.username == USERNAME
        and form_data.password == PASSWORD
    ):

        # Create JWT token

        token = jwt.encode(
            {
                "username": form_data.username
            },
            SECRET_KEY,
            algorithm=ALGORITHM
        )

        # IMPORTANT OAuth2 format

        return {
            "access_token": token,
            "token_type": "bearer"
        }


    raise HTTPException(
        status_code=401,
        detail="Wrong username or password"
    )


# =====================================
# PROTECTED PROFILE
# =====================================

@app.get("/profile")
def profile(
    token: str = Depends(oauth2_scheme)
):

    data = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM]
    )

    return {
        "message": "Profile accessed successfully",
        "username": data["username"]
    }
