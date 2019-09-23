from django.contrib import admin

# Register your models here.

from .models import PointsTable

class CourseAdmin(admin.ModelAdmin):
    ordering = ['-points']
    list_display = ('team_name', 'played', 'won', 'lost', 'no_result','points','nrr')

admin.site.register(PointsTable, CourseAdmin)
