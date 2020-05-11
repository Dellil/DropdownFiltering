from django.contrib import admin
from . import models


@admin.register(models.School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "kind",
        "id"
    )

    ordering = ["kind"]

@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "school",
        "id"
    )

    ordering = ["name"]
