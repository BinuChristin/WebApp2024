from django.contrib import admin

from .models import Post, Category

# Register your models here.
admin.site.register(Post)
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('post_title', 'post_author')
#     date_hierarchy = 'post_publish_datatime'
#     search_fields = ('post_shortname', 'post_description')
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','slug']
    prepopulated_fields = {'slug':('title',)}