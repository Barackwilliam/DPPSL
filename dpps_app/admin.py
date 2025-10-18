from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Service,User_Testimonial

from .forms import  ServiceAdminForm,BlogPostForm, User_TestimonialForm,CertificateUploadForm

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


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Training, Participant

class ParticipantInline(admin.StackedInline):
    model = Participant
    can_delete = False
    verbose_name_plural = 'Taarifa za Mshiriki'
    readonly_fields = ['date_registered']

class CustomUserAdmin(UserAdmin):
    inlines = [ParticipantInline]
    list_display = ['username', 'email', 'get_full_name', 'get_status', 'date_joined']
    list_filter = ['participant__status', 'date_joined']
    
    def get_full_name(self, obj):
        if hasattr(obj, 'participant'):
            return obj.participant.full_name
        return "-"
    get_full_name.short_description = "Jina Kamili"
    
    def get_status(self, obj):
        if hasattr(obj, 'participant'):
            return obj.participant.get_status_display()
        return "-"
    get_status.short_description = "Hali"

@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_date', 'end_date']
    list_filter = ['start_date', 'end_date']
    search_fields = ['title']


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    form = CertificateUploadForm
    list_display = ['full_name', 'user', 'training', 'participation_date', 'status', 'certificate_uploaded']
    list_filter = ['status', 'training', 'participation_date']
    search_fields = ['full_name', 'user__username', 'organization']
    readonly_fields = ['date_registered']
    actions = ['approve_participants', 'reject_participants']

    def approve_participants(self, request, queryset):
        queryset.update(status='approved')
    approve_participants.short_description = "Approve selected participants"

    def reject_participants(self, request, queryset):
        queryset.update(status='rejected')
    reject_participants.short_description = "Reject selected participants"

    fieldsets = (
        (None, {
            'fields': ('user', 'full_name', 'phone_number')
        }),
        ('Training Details', {
            'fields': ('training', 'participation_date', 'status')
        }),
        ('Organization', {
            'fields': ('organization', 'position')
        }),
        ('Certificate', {
            'fields': ('certificate',),
            'description': 'Upload certificate file (PDF, DOCX, etc.) via Uploadcare. Supported formats are automatically handled.'
        }),
        ('Metadata', {
            'fields': ('date_registered',),
            'classes': ('collapse',)
        }),
    )
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)