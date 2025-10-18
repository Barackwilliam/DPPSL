from django.db import models
from pyuploadcare.dj.models import ImageField  
# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=255, blank=True, null=True)  # Hifadhi Uploadcare UUID au URL

    def __str__(self):
        return self.title

    # Kwa Open Graph preview (Facebook, WhatsApp etc.)
    def get_og_image_url(self):
        if self.image:
            return f"https://ucarecdn.com/{self.image}/-/resize/1200x630/-/format/auto/"
        return ''

    # Kwa matumizi ya kawaida kwenye site (speed optimized)
    def get_image_url(self):
        if self.image:
            return f"https://ucarecdn.com/{self.image}/-/format/jpg/-/quality/smart/"
        return ''



class Team(models.Model):
    Full_name = models.CharField(max_length=100)
    image = models.CharField(max_length=255, blank=True, null=True)  # Uploadcare image URL
    designation = models.TextField()
    facebook_link = models.URLField(max_length=300, blank=True, null=True)
    twitter_link = models.URLField(max_length=300, blank=True,  null=True)
    instagram_link = models.URLField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.Full_name

    # Kwa Open Graph preview
    def get_og_image_url(self):
        return f"https://ucarecdn.com/{self.image}/-/resize/1200x630/-/format/auto/"

    # Kwa frontend display optimized
    def get_image_url(self):
        return f"https://ucarecdn.com/{self.image}/-/format/jpg/-/quality/smart/"
   


class User_Testimonial(models.Model):
    Full_name = models.CharField(max_length=100)
    image = ImageField(blank=True, null=True, manual_crop="")  # Use ImageField for images; stores UUID automatically    
    comment = models.TextField()   # badala ya description
    profession = models.CharField(max_length=100)

    def __str__(self):
        return self.Full_name

    # Kwa Open Graph preview
    def get_og_image_url(self):
        if self.image:
            return f"https://ucarecdn.com/{self.image}/-/resize/1200x630/-/format/auto/"
        return "https://ucarecdn.com/09cf22be-f6f4-4d5a-abbd-1de08520e7e3/-/resize/1200x630/-/format/auto/"

    # Kwa frontend display optimized
    def get_image_url(self):
        if self.image:
            return str(self.image)  # ImageField provides URL via Uploadcare CDN
        return "https://ucarecdn.com/09cf22be-f6f4-4d5a-abbd-1de08520e7e3/-/format/jpg/-/quality/smart/"


from django.db import models
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)  # Uploadcare or URL
    summary = models.TextField()
    content = models.TextField()
    author = models.CharField(max_length=100, default="DPPS Team")
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_image_url(self):
        if self.image:
            return f"https://ucarecdn.com/{self.image}/-/format/jpg/-/quality/smart/"
        return "https://ucarecdn.com/09cf22be-f6f4-4d5a-abbd-1de08520e7e3/-/format/jpg/-/quality/smart/"


from django.db import models

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question



class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject or 'No Subject'}"

from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.core.validators import FileExtensionValidator
from pyuploadcare.dj.models import FileField
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator  # Add this import
from pyuploadcare.dj.forms import FileWidget   # Correct import for the widget (from forms, not widgets)


class Training(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} ({self.start_date} - {self.end_date})"


# Mfano tu wa Training model (hakikisha ipo kwenye models zako)
# from .models import Training


class Participant(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200, verbose_name="Full Name")
    phone_number = models.CharField(max_length=20, verbose_name="Phone Number")
    organization = models.CharField(max_length=200, verbose_name="Organization", blank=True)
    position = models.CharField(max_length=100, verbose_name="Position", blank=True)
    training = models.ForeignKey('Training', on_delete=models.CASCADE, verbose_name="Training")
    participation_date = models.DateField(null=True, blank=True, verbose_name="Participation Date")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    # Uploadcare integration for PDF, DOCX, etc.
    certificate = FileField(
        blank=True,
        null=True,
        verbose_name="Certificate File",
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'doc'])]
    )

    date_registered = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.participation_date and (
            self.participation_date < self.training.start_date or
            self.participation_date > self.training.end_date
        ):
            raise ValidationError("The participation date must be within the training period.")

    def __str__(self):
        return self.full_name

    @property
    def certificate_uploaded(self):
        return bool(self.certificate)

    class Meta:
        verbose_name = "Participant"
        verbose_name_plural = "Participants"

