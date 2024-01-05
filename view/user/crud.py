from view.user.schemas import Create_user

def create_user(user_in: Create_user) -> dict:
    user = user_in.model_dump()
    return {
        "success": True,
        "user": user,
    }