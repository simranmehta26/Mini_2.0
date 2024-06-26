from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
class UserManager123(BaseUserManager):
    def create_user(self, email, student_name, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, student_name=student_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, student_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, student_name, password, **extra_fields)

class User123(AbstractBaseUser):
    student_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  
    dob = models.DateField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager123()

class QuestionsTable(models.Model):
    QId = models.CharField(max_length=25, unique=True)
    Question = models.TextField(default=True)
    Option1 = models.TextField(default=True)
    Option2 = models.TextField(default=True)
    Option3 = models.TextField(default=True)
    Option4 = models.TextField(default=True)
    Answer = models.TextField(default=True)
    Q_type = models.TextField(default=True)

    def __str__(self):
        return self.name

class HSBCQuestions(models.Model):
    QId = models.CharField(max_length=25, unique=True)
    Question = models.TextField(default=True)
    Option1 = models.TextField(default=True)
    Option2 = models.TextField(default=True)
    Option3 = models.TextField(default=True)
    Option4 = models.TextField(default=True)
    Answer = models.TextField(default=True)
    Q_type = models.TextField(default=True)

    def __str__(self):
        return self.name
    

class ContactMessage(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class TechMQuestions(models.Model):
    QId = models.CharField(max_length=25, unique=True)
    Question = models.TextField(default=True)
    Option1 = models.TextField(default=True)
    Option2 = models.TextField(default=True)
    Option3 = models.TextField(default=True)
    Option4 = models.TextField(default=True)
    Answer = models.TextField(default=True)
    Q_type = models.TextField(default=True)

    def __str__(self):
        return self.name