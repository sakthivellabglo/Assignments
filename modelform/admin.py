from django.contrib import admin
from .models import *

class display_students(admin.ModelAdmin):
	list_display = ('id','first_name', 'last_name', 'img')

admin.site.register(stu, display_students)
admin.site.register(mark)

# Register your models here.
