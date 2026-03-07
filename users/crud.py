from users.schemas import CreateUser


def create_user(user_in: CreateUser) -> dict[str, bool | dict]:
    user = user_in.model_dump()
    return {"status": True, "user": user}
