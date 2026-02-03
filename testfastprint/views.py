from django.views.generic import CreateView


class RedirectView(CreateView) :
    template_name = "redirect.html"
