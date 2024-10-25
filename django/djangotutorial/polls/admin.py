from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Choice, Question

admin.site.site_header = "Poll Management Admin Portal"
# admin.site.index_title = "Welcome to the FEEL GOOD FRIDAY!"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
    class Media:   
        css = {
             'all': ('templates/admin/base_site.css',)
        }

# class QuestionResource(resources.ModelResource):
#     def for_delete(self, row, instance):
#         return row["delete"] == "1"
    
#     class Meta:
#         model = Question
admin.site.register(Question, QuestionAdmin)
