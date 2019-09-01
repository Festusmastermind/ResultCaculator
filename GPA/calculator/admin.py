from django.contrib import admin
from calculator.models import StudentProfile, Result
from import_export.admin import ImportExportModelAdmin

# admin.site.register(StudentProfile)
# admin.site.register(Result)
@admin.register(Result, StudentProfile)

class ViewAdmin(ImportExportModelAdmin):
    pass