from typing import Annotated
from annotated_types import MinLen, MaxLen

from pydantic import BaseModel, EmailStr

class Create_user(BaseModel):
    user_name: Annotated[str, MinLen(3), MaxLen(25)]
    email: EmailStr