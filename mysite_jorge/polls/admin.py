from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model=Choice

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Principal',        {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    list_per_page = 10




admin.site.register(Question, QuestionAdmin)