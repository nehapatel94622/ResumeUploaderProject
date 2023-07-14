from django.contrib import admin
from .models import ResumeModel

# Register your models here.


@admin.register(ResumeModel)
class ResumeModelAdmin(admin.ModelAdmin):
    list_display = ("my_file", "profile_image", "job_city", "email", "mobile", "state", "Pin", "city", "locality", "gender", "dob", "name", "id")[::-1]
