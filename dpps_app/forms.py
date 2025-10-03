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




class User_TestimonialForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'

    class Media:
        js = [
            'https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js',
        ]


from .models import BlogPost

# class BlogPostForm(forms.ModelForm):
#     class Meta:
#         model = BlogPost
#         fields = ['title', 'category', 'image', 'summary', 'content', 'author']
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'category': forms.TextInput(attrs={'class': 'form-control'}),
#             'image': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Uploadcare image URL'}),
#             'summary': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
#             'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
#             'author': forms.TextInput(attrs={'class': 'form-control'}),
#         }
#     class Media:
#             js = [
#                 'https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js',
#             ]


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'

    class Media:
        js = [
            'https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js',
        ]
