from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .models import Recipe
from recipes.forms import RecipeForm

# Create your views here.

class MainView(LoginRequiredMixin, View):
    def get(self, request):
        recipe=Recipe.objects.all()
        ctx={"recipe_list":recipe}
        return render(request, "recipes/recipe_list.html", ctx)


class OpenView(View):
    def get(self, request):
        return render(request, "recipes/logout_view.html")

class RecipeCreateView(View):
    def get(self, request):
        form = RecipeForm()
        context = {"form":form}
        return render(request,"recipes/recipe_form.html", context)

    def post(self, request):
        form = RecipeForm(request.POST)
        if not form.is_valid():
            context = { "form":form }
            return render(request,"recipes/recipe_form.html", context)

        recipe = form.save()
        return render(request, "recipes/recipe_success.html")

