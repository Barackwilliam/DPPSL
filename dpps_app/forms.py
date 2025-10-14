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
