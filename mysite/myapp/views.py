from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from . import models
from . import forms


def index(request):
    context = {
            "title":"Greetings",
            "opener":"Hello World",
            "initialStatement":" This is the beginnings of the greatest recipe website known to man",
            }
    return render(request, "index.html", context=context)


def home(request):
    value = models.Recipe.objects.all()
    context = {
            "title":"Recipes",
            "opener":"Recipes",
            #"addRecipeUrl":"/add/",
            "add":"/add/",
            "view":"/view/",
            "review":"/review/",
            "login":"/login/",
            "recipeList":value,
            }
    return render(request, "home.html", context=context)

@login_required(login_url='/login/')
def addRecipe(request):
    if request.method == "POST":
        form_instance = forms.RecipeForm(request.POST, request.FILES)
        if form_instance.is_valid():
            new_reci = form_instance.save(request=request)
            return redirect("/")
    else:
        form_instance = forms.RecipeForm()

    context = {
            "title":"Add",
            "opener":"Add Recipe",
            "add":"/add/",
            "view":"/view/",
            "review":"/review/",
            "login":"/login/",
            "form":form_instance,
            }
    return render(request, "add.html", context=context)


def viewRecipe(request):
    context = {
            "title":"Recipe",
            "opener":"View Recipe",
            "reviewRecipeUrl":"/review/",
            "add":"/add/",
            "view":"/view/",
            "review":"/review/",
            "login":"/login/",
            }
    return render(request, "viewRecipe.html", context=context)

def reviewRecipe(request):
    context = {
            "title":"Review",
            "opener":"Review Recipe",
            "add":"/add/",
            "view":"/view/",
            "review":"/review/",
            "login":"/login/",
            }
    return render(request, "review.html", context=context)

def register(request):
    if request.method == "POST":
        form_instance = forms.RegistrationForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("/login/")
    else:
        form_instance = forms.RegistrationForm()
    context = {
        "form":form_instance,
        "login":"/login/",
    }
    return render(request, "registration/register.html", context=context)



