from django.contrib import admin

from .models import (
    Application,
    Job,
    Opening,
    Organization,
    Resume,
    TeamMember,
    Testimonial,
    Certification,
    WorkExperience,
)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
    )


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
    )


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "job",
        "created_date",
    )


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    pass


@admin.register(Opening)
class OpeningAdmin(admin.ModelAdmin):
    pass


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    pass


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    pass


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    pass

