from django.urls import path

from .views import (About, ApplicationCreateView, Blog, Contact, Hire, Home,
                    JobCreateView, JobDetailView, Openings, People, Privacy,
                    Selection, ShareOpening, SubmitResume, Terms)

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("apply/job/<job_pk>/", ApplicationCreateView.as_view(), name="apply_job"),
    path("about/", About.as_view(), name="about"),
    path("people/", People.as_view(), name="people"),
    path("openings/", Openings.as_view(), name="openings"),
    path("openings/new/", ShareOpening.as_view(), name="share_opening"),
    path("jobs/new/", JobCreateView.as_view(), name="create_job"),
    path("jobs/<pk>/<slug>/", JobDetailView.as_view(), name="view_job"),
    path("submit_resume/", SubmitResume.as_view(), name="submit_resume"),
    path("selection_process/", Selection.as_view(), name="selection"),
    path("hire/", Hire.as_view(), name="hire"),
    path("blog/", Blog.as_view(), name="blog"),
    path("contact/", Contact.as_view(), name="contact"),
    path("privacy/", Privacy.as_view(), name="privacy"),
    path("terms/", Terms.as_view(), name="terms"),
]
