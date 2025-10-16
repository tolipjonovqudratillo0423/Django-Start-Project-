from django.contrib import admin

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')