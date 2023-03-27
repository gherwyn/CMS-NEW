from django.contrib import admin
from .models import Projects, Comment
from django.contrib.contenttypes.admin import GenericTabularInline
# Register your models here.

admin.site.site_header = "Wizzard Projects Monitoring"
admin.site.site_title = "Project Monitoring Admin"
admin.site.index_title = "Projects List"


class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0

class UserAdmin(admin.ModelAdmin):
    list_display = ['image_tag','user_fname','user_lname','user_email','user_position']
    search_fields = ['user_fname','user_lname','user_email','user_position']
    inlines = [CommentInLine]

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','body','projects_id','created_on','active')
    list_filter = ('active','created_on')
    search_fields = ('name','email','body')
    actions = ['approve_comment']

    def approve_comment(self, request, queryset):
        queryset.update(active=True)





admin.site.register(Projects, UserAdmin)
admin.site.register(Comment, CommentAdmin)

