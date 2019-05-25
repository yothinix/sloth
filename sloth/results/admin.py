from django.contrib import admin


from .models import Result


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('app_name', 'class_name', 'test_name', 'time')
    # list_filter  = ('app_name',)
    ordering = ('time',)
