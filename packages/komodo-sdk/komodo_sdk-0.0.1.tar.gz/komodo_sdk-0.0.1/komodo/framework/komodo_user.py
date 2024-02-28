class KomodoUser:
    def __init__(self, user_id, email, name, role, plan, verified, allowed_assistants, preferred_assistant):
        self.user_id = user_id
        self.email = email
        self.name = name
        self.role = role
        self.plan = plan
        self.verified = verified
        self.allowed_assistants = allowed_assistants
        self.preferred_assistant = preferred_assistant

    def __str__(self):
        return f"KomodoUser(user_id={self.user_id}, email={self.email}, name={self.name}, role={self.role}, plan={self.plan}, verified={self.verified}, allowed_assistants={self.allowed_assistants}, preferred_assistant={self.preferred_assistant})"

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'email': self.email,
            'name': self.name,
            'role': self.role,
            'plan': self.plan,
            'verified': self.verified,
            'allowed_assistants': self.allowed_assistants,
            'preferred_assistant': self.preferred_assistant}

    @classmethod
    def default_user(cls):
        user_id = "ryan.oberoi@komodoapp.ai"
        return cls(user_id=user_id, email=user_id, name="Ryan Oberoi", role="user", plan="free", verified=True,
                   allowed_assistants=[], preferred_assistant="")
