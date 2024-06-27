from django.contrib import admin
from myApp.models import Student
class StudentAdmin(admin.ModelAdmin):
 l=['sno','sname','smarks','saddr']
admin.site.register(Student,StudentAdmin)
