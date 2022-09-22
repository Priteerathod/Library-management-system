from django.contrib import admin
from testapp.models import Book
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display=['name','author','price','p_date']
admin.site.register(Book,BookAdmin)
