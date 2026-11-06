class UserService:
    """Manage user information."""

    def get_user(self, user_id):
        """Find a user by ID."""
        return {"id": user_id}

    def create_user(self, name, email):
        """Create a new user."""
        return {
            "name": name,
            "email": email
        }
      
