from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
	def get(self, request, **kwargs):
			return render(request, 'index.html', context=None)

class SearchPageView(TemplateView):
	template_name = "Search.html"

class CollectPageView(TemplateView):
	template_name = "Collection.html"

class AboutPageView(TemplateView):
	template_name = "About.html"

class SignInPageView(TemplateView):
	template_name = "signin.html"