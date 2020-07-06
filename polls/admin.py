from django.contrib import admin

from .models import Question, Choice


# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    list_display = ['text', 'vote']


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['body', 'publish']
    list_filter = ['publish']
    search_fields = ['body']
    inlines = [
        ChoiceInline,
    ]


admin.site.register(Question, QuestionAdmin)