from django.contrib import admin
from .models import Book
# Register your models here.
   
def mark_as_classic(modeladmin, request, queryset):
        queryset.update(title='Classic: ' + queryset[0].title)

mark_as_classic.short_description = "Mark selected books as classic"

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'author')
    list_filter = ('published_date', 'author')
    ordering = ('published_date', ) 
    list_editable = ('author',)
    actions = [mark_as_classic]   


    
admin.site.register(Book, BookAdmin)