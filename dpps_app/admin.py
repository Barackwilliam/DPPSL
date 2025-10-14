from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Service,User_Testimonial

from .forms import  ServiceAdminForm,BlogPostForm, User_TestimonialForm

# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
    form = ServiceAdminForm

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'image':
            formfield.widget.attrs.update({
                'role': 'uploadcare-uploader',
                'data-public-key': '76122001cca4add87f02', 
            })
        return formfield

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.get_image_url()}" style="max-height: 100px;" />')
        return "No Image"

    image_preview.short_description = 'Preview'

    list_display = ('title', 'image_preview')

admin.site.register(Service, ServiceAdmin)



from .models import Team
from .forms import TeamForm

class TeamAdmin(admin.ModelAdmin):
    form = TeamForm

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'image':
            formfield.widget.attrs.update({
                'role': 'uploadcare-uploader',
                'data-public-key': '76122001cca4add87f02', 
            })
        return formfield

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.get_image_url()}" style="max-height: 100px;">')
        return "No Image"

    image_preview.short_description = 'Image Preview'

    list_display = ('Full_name', 'designation', 'image_preview')

admin.site.register(Team, TeamAdmin)


class UserTestimonialAdmin(admin.ModelAdmin):
    form = User_TestimonialForm

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'image':
            formfield.widget.attrs.update({
                'role': 'uploadcare-uploader',
                'data-public-key': '76122001cca4add87f02',
            })
        return formfield

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.get_image_url()}" style="max-height: 100px;" />')
        return "No Image"

    image_preview.short_description = 'Preview'

    list_display = ('Full_name', 'profession', 'image_preview')

admin.site.register(User_Testimonial, UserTestimonialAdmin)


from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostForm

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'image':
            formfield.widget.attrs.update({
                'role': 'uploadcare-uploader',
                'data-public-key': '76122001cca4add87f02',
            })
        return formfield

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.get_image_url()}" style="max-height: 100px;" />')
        return "No Image"

    image_preview.short_description = 'Preview'

    list_display = ('title', 'category', 'author', 'created_at')
    search_fields = ('title', 'category', 'author')
    list_filter = ('category', 'created_at')



admin.site.register(BlogPost, BlogPostAdmin)


from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "created_at")
    search_fields = ("question", "answer")

from .models import ContactMessage

admin.site.register(ContactMessage)
