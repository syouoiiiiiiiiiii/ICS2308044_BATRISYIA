from django.contrib import admin
from .models import Course,Student,Mentor,Book,Borrowing
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Mentor)
admin.site.register(Book)
admin.site.register(Borrowing)

# Register your models here.
