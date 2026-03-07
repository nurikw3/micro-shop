from typing import Annotated
from pydantic import BaseModel, EmailStr
from annotated_types import MaxLen, MinLen


class CreateUser(BaseModel):
    nick: Annotated[str, MinLen(10), MaxLen(15)]
    email: EmailStr
