from django.conf import settings
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    FormView,
    ListView,
    TemplateView,
)

from .forms import ApplicationForm, ContactForm, JobForm, OpeningForm, ResumeForm
from .models import (
    FUNCTION_CHOICES,
    INDUSTRY_CHOICES,
    LEVEL_CHOICES,
    TIME_ZONE_CHOICES,
    TYPE_CHOICES,
    Application,
    Job,
    Opening,
    Resume,
)
from .utils import send_email

# Create your views here.


class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        ctx = super(Home, self).get_context_data(**kwargs)

        ctx["section"] = "home"
        ctx["page_title"] = "Welcome to Hash Academy"
        ctx["meta_description"] = ""
        ctx["jobs"] = Job.objects.all()
        return ctx


class About(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        ctx = super(About, self).get_context_data(**kwargs)
        ctx["section"] = "about"
        ctx["page_title"] = "Who We Are"
        ctx["meta_description"] = ""
        return ctx


class People(TemplateView):
    template_name = "people.html"

    def get_context_data(self, **kwargs):
        ctx = super(People, self).get_context_data(**kwargs)
        ctx["section"] = "people"
        ctx["page_title"] = "Our People"
        ctx["meta_description"] = ""
        return ctx


class Openings(ListView):
    model = Job
    context_object_name = "jobs"
    template_name = "openings.html"

    def get_queryset(self):
        jobs = Job.objects.all()

        if self.request.GET.get("title"):
            query = self.request.GET.get("title")
            jobs = jobs.filter(Q(title__icontains=query))
        if self.request.GET.get("function"):
            query = self.request.GET.get("function")
            jobs = jobs.filter(Q(functions__icontains=query))
        if self.request.GET.get("industry"):
            query = self.request.GET.get("industry")
            jobs = jobs.filter(Q(industry__icontains=query))
        if self.request.GET.get("type"):
            query = self.request.GET.get("type")
            jobs = jobs.filter(Q(type__icontains=query))
        if self.request.GET.get("level"):
            query = self.request.GET.get("level")
            jobs = jobs.filter(level__gte=query)
        if self.request.GET.get("timezone"):
            query = self.request.GET.get("timezone")
            jobs = jobs.filter(timezone=query)

        return jobs

    def get_context_data(self, **kwargs):
        ctx = super(Openings, self).get_context_data(**kwargs)

        functions = dict(FUNCTION_CHOICES)
        industries = dict(INDUSTRY_CHOICES)
        types = dict(TYPE_CHOICES)
        levels = dict(LEVEL_CHOICES)
        timezones = dict(TIME_ZONE_CHOICES)

        searched_title = ""
        if self.request.GET.get("title"):
            searched_title = self.request.GET.get("title")
        sel_function = ""
        if self.request.GET.get("function"):
            sel_function = self.request.GET.get("function")
        sel_industry = ""
        if self.request.GET.get("industry"):
            sel_industry = self.request.GET.get("industry")
        sel_type = ""
        if self.request.GET.get("type"):
            sel_type = self.request.GET.get("type")
        sel_level = ""
        if self.request.GET.get("level"):
            sel_level = int(self.request.GET.get("level"))
        sel_timezone = ""
        if self.request.GET.get("timezone"):
            sel_timezone = int(self.request.GET.get("timezone"))

        ctx["functions"] = functions
        ctx["industries"] = industries
        ctx["industries"] = industries
        ctx["types"] = types
        ctx["levels"] = levels
        ctx["timezones"] = timezones
        ctx["searched_title"] = searched_title
        ctx["sel_function"] = sel_function
        ctx["sel_industry"] = sel_industry
        ctx["sel_type"] = sel_type
        ctx["sel_level"] = sel_level
        ctx["sel_timezone"] = sel_timezone

        ctx["section"] = "openings"
        ctx["page_title"] = "Current Openings"
        ctx["meta_description"] = ""

        return ctx


class JobDetailView(DetailView):
    model = Job
    template_name = "job_detail.html"
    context_object_name = "job"

    def get_context_data(self, **kwargs):
        ctx = super(JobDetailView, self).get_context_data(**kwargs)
        ctx["section"] = "jobs"
        ctx["page_title"] = self.object.title
        ctx["meta_description"] = self.object.description
        ctx["organization"] = self.object.organization
        return ctx


class SubmitResume(CreateView):
    model = Resume
    template_name = "submit_resume.html"
    form_class = ResumeForm

    def get_context_data(self, **kwargs):
        ctx = super(SubmitResume, self).get_context_data(**kwargs)
        ctx["section"] = "submit_resume"
        ctx["page_title"] = "Submit Resume"
        ctx["meta_description"] = ""
        return ctx

    def form_valid(self, form):
        resume = form.save(commit=False)
        resume.save()
        messages.success(
            self.request,
            "Your resume has been successfully submitted. We will get back to you shortly",
            extra_tags="alert-success",
        )
        return super(SubmitResume, self).form_valid(form)

    def get_success_url(self):
        return reverse("home")


class Selection(TemplateView):
    template_name = "selection.html"

    def get_context_data(self, **kwargs):
        ctx = super(Selection, self).get_context_data(**kwargs)
        ctx["section"] = "selection"
        ctx["page_title"] = "Our Selection Process"
        ctx["meta_description"] = ""
        return ctx


class Hire(TemplateView):
    template_name = "hire.html"

    def get_context_data(self, **kwargs):
        ctx = super(Hire, self).get_context_data(**kwargs)
        ctx["section"] = "hire"
        ctx["page_title"] = "Hire from Hash Academy"
        ctx["meta_description"] = ""
        return ctx


class Blog(TemplateView):
    template_name = "contact.html"

    def get_context_data(self, **kwargs):
        ctx = super(Blog, self).get_context_data(**kwargs)
        ctx["section"] = "blog"
        ctx["page_title"] = "Our Blog"
        ctx["meta_description"] = ""
        return ctx


class Contact(FormView):
    template_name = "contact.html"
    form_class = ContactForm

    def form_valid(self, form):
        subject = "Message from Hash Academy Contact Form"
        from_email = form.cleaned_data.get("from_email")
        message = render_to_string(
            "partials/contact_message.html",
            {
                "subject": form.cleaned_data.get("subject"),
                "name": form.cleaned_data.get("name"),
                "message": form.cleaned_data.get("message"),
            },
        )
        to_email = settings.DEFAULT_FROM_EMAIL
        send_email(subject, message, to_email, from_email)
        messages.success(
            self.request,
            "Thank you for getting in touch. We will get back to you shortly",
            extra_tags="alert-success",
        )
        return super(Contact, self).form_valid(form)

    def get_success_url(self):
        return reverse("contact")

    def get_context_data(self, **kwargs):
        ctx = super(Contact, self).get_context_data(**kwargs)
        ctx["form"] = ContactForm()
        ctx["section"] = "contact"
        ctx["page_title"] = "Contact us"
        ctx["meta_description"] = ""
        return ctx


class Privacy(TemplateView):
    template_name = "privacy.html"

    def get_context_data(self, **kwargs):
        ctx = super(Privacy, self).get_context_data(**kwargs)
        ctx["section"] = "privacy"
        ctx["page_title"] = "Privacy Policy"
        ctx["meta_description"] = ""
        return ctx


class Terms(TemplateView):
    template_name = "terms.html"

    def get_context_data(self, **kwargs):
        ctx = super(Terms, self).get_context_data(**kwargs)
        ctx["section"] = "terms"
        ctx["page_title"] = "Terms and Conditions"
        ctx["meta_description"] = ""
        return ctx


class ApplicationCreateView(CreateView):
    model = Application
    template_name = "application_form.html"
    form_class = ApplicationForm

    def get_context_data(self, **kwargs):
        ctx = super(ApplicationCreateView, self).get_context_data(**kwargs)
        job = Job.objects.get(pk=self.kwargs["job_pk"])
        ctx["section"] = "application"
        ctx["page_title"] = "Apply for {}".format(job.title)
        ctx["meta_description"] = ""
        return ctx

    def form_valid(self, form):
        application = form.save(commit=False)
        job = Job.objects.get(pk=self.kwargs["job_pk"])
        applications = job.job_applications.all()
        user_applications = applications.filter(
            email_address=form.cleaned_data.get("email_address")
        )
        if len(user_applications) > 0:
            messages.warning(
                self.request,
                "You have already applied for this job.",
                extra_tags="alert-warning",
            )
            return HttpResponseRedirect(self.request.META.get("HTTP_REFERER"))
        else:
            application.job = job
            application.save()
            messages.success(
                self.request,
                "Your application has been successfully submitted. We will get back to you shortly",
                extra_tags="alert-success",
            )
        return super(ApplicationCreateView, self).form_valid(form)

    def get_success_url(self):
        job = Job.objects.get(pk=self.kwargs["job_pk"])
        return job.get_absolute_url()


class JobCreateView(CreateView):
    model = Job
    template_name = "job_form.html"
    form_class = JobForm

    def get_context_data(self, **kwargs):
        ctx = super(JobCreateView, self).get_context_data(**kwargs)
        ctx["section"] = "create_job"
        ctx["page_title"] = "Submit a job opening"
        ctx["meta_description"] = ""
        return ctx

    def form_valid(self, form):
        job = form.save(commit=False)
        job.save()
        messages.success(
            self.request,
            "The job has been successfully created.",
            extra_tags="alert-success",
        )
        # Without this next line the tags won't be saved.
        form.save_m2m()
        return super(JobCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("home")


class ShareOpening(CreateView):
    model = Opening
    template_name = "share_opening.html"
    form_class = OpeningForm

    def get_context_data(self, **kwargs):
        ctx = super(ShareOpening, self).get_context_data(**kwargs)
        ctx["section"] = "share_opening"
        ctx["page_title"] = "Post a job opening"
        ctx["meta_description"] = ""
        return ctx

    def form_valid(self, form):
        opening = form.save(commit=False)
        opening.save()
        messages.success(
            self.request,
            "Your job opening has been successfully submitted. We will get back to you shortly",
            extra_tags="alert-success",
        )
        return super(ShareOpening, self).form_valid(form)

    def get_success_url(self):
        return reverse("home")
