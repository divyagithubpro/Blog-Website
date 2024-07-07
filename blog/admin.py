from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'approved')
    list_editable = ('approved',)

admin.site.register(Post, PostAdmin)
