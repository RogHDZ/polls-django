from django.contrib import admin

from .models import Choice, Question

# Register your models here.
#admin.site.register(Question)
#admin.site.register(Choice)


class ChoiceInLine(admin.TabularInline):
    model = Choice


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLine]