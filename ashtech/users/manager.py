from django.contrib.auth.models import BaseUserManager
from django.utils import  timezone

class UserManager(BaseUserManager):
    def _create_user(self, email, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError("User Must Have Email")
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )

        # set password
        user.set_password(password)
        user.save(using=self._db)
        return user

    #create new user
    def create_user(self, email, password, **extrafields):
        return self._create_user(email, password, False, False, **extrafields)

    def create_superuser(self, email, password, **extrafields):
        user = self._create_user(email, password, True, True, **extrafields)
        user.save(using=self._db)
        return user