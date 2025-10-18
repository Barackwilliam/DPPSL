from django import forms
from .models import Service,Team,User_Testimonial


class ServiceAdminForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

    class Media:
        js = [
            'https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js',
        ]




class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'

    class Media:
        js = [
            'https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js',
        ]



from pyuploadcare.dj.forms import FileWidget  # Import this

class User_TestimonialForm(forms.ModelForm):
    class Meta:
        model = User_Testimonial
        fields = ['Full_name', 'profession', 'image', 'comment']
        widgets = {
            'Full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Full Name'}),
            'profession': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Profession'}),
            'image': FileWidget(attrs={
                'data-public-key': '76122001cca4add87f02',  # Optional if set in settings; replace if needed
                'data-images-only': 'true',  # Restrict to images
                'data-max-size': '5242880',  # 5MB limit
            }),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Share your experience...', 'rows': 5}),
        }

    class Media:
        js = ('https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js',)  # Ensure JS loads


from .models import BlogPost
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'

    class Media:
        js = [
            'https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js',
        ]

from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control border-0', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control border-0', 'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control border-0', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control border-0', 'placeholder': 'Leave your message here', 'style': 'height:160px;'}),
        }

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Participant, Training
from datetime import date


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email Address")
    full_name = forms.CharField(max_length=200, required=True, label="Full Name")
    phone_number = forms.CharField(max_length=20, required=True, label="Phone Number")
    organization = forms.CharField(max_length=200, required=False, label="Organization (Optional)")
    position = forms.CharField(max_length=100, required=False, label="Position (Optional)")
    training = forms.ModelChoiceField(queryset=Training.objects.filter(end_date__gte=date.today()), label="Select Training")

    class Meta:
        model = User
        fields = ['username', 'email', 'full_name', 'phone_number', 'organization', 'position', 'training', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['training', 'participation_date']
        widgets = {
            'participation_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['training'].queryset = (
            self.fields['training'].queryset.filter(end_date__gte=date.today())
        )



class CertificateUploadForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['certificate']
        widgets = {
            'certificate': FileWidget(attrs={
                'data-public-key': '76122001cca4add87f02',  # 🔑 weka Uploadcare public key yako halisi
            }),
        }
class CertificateUploadForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['certificate']
        widgets = {
            'certificate': FileWidget(attrs={
                'data-public-key': '76122001cca4add87f02',  # 🔑 weka Uploadcare public key yako halisi
            }),
        }
class CertificateUploadForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['certificate']
        widgets = {
            'certificate': FileWidget(attrs={
                'data-public-key': '76122001cca4add87f02',  # 🔑 weka Uploadcare public key yako halisi
            }),
        }

        
class CertificateUploadForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['certificate']
        widgets = {
            'certificate': FileWidget(attrs={
                'data-public-key': '76122001cca4add87f02',  # 🔑 weka Uploadcare public key yako halisi
            }),
        }
