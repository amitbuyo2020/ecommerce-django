from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    # Creating process of a user
    def create_user(self, email, username, password, **extra_fields):
        # retrieve values of email, username and password from the login form
        if not email and username:
            raise ValueError("Username and Email are required")

        email = self.normalize_email(email)
        # normalize_email is only available for BaseUserManager
        # normalizes the characters of email to lower case

        # Create a user model with email and username
        user = self.model(
            email = email,
            username = username,
            **extra_fields 
        )  
        # Set the password for the formed user model
        user.set_password(password)
        # save the user model to the database
        user.save(using=self._db)

        return user

    #CREATING A SUPER USER
    def create_superuser(self, email, username, password, **extra_fields):
        # Creating a default value for a superuser
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)

        # check the default value of the superuser
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Super User must have is_staff = True")

        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Super User must have is_superuser = True")
            
        
        # returns the create_user function to create superuser which have all the 
        # functionality of a normal user but also have some premissions and privileges
        return self.create_user(email, username, password, **extra_fields)
