from django.db import models

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
    twitter_link = models.URLField(max_length=300, blank=True, null=True)
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
    Full_name =  models.CharField(max_length=100)
    image = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField()   # badala ya description
    profession = models.CharField(max_length=100) 
    def __str__(self):
        return self. Full_name

    # Kwa Open Graph preview
    def get_og_image_url(self):
        return f"https://ucarecdn.com/{self.image}/-/resize/1200x630/-/format/auto/"

    # Kwa frontend display optimized
    def get_image_url(self):
        return f"https://ucarecdn.com/{self.image}/-/format/jpg/-/quality/smart/"


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
        return "/static/img/default-blog.jpg"


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
