from django.shortcuts import render
from django.views import View


class HomeView(View):
    template_name = 'core/home.html'
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        return render(request, self.template_name, self.context)