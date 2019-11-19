from django.shortcuts import render, redirect
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
            "add":"/add/",
            "view":"/view/",
            "login":"/login/",
            "logout":"/logout/",
            "recipeList":value,
            }
    return render(request, "home.html", context=context)

@login_required(login_url='/login/')
def addRecipe(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            form_instance = forms.RecipeForm(request.POST, request.FILES)
            if form_instance.is_valid():
                new_reci = form_instance.save(request=request)
                return redirect("/ingredient/" + str(new_reci.id))
        else:
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
            "logout":"/logout/",
            "form":form_instance,
            }
    return render(request, "add.html", context=context)


@login_required(login_url='/login/')
def viewRecipe(request,instance_id):
    instance = models.Recipe.objects.get(id=instance_id)
    context = {
            "title":"Recipe",
            "opener":"View Recipe",
            "reviewRecipeUrl":"/review/",
            "add":"/add/",
            "review":"/review/",
            "login":"/login/",
            "logout":"/logout/",
            "foodCategory":instance.get_foodCategory_display(),
            "Recipe":instance,
            "reci_id":instance_id,
            }
    return render(request, "viewRecipe.html", context=context)

@login_required(login_url='/login/')
def reviewRecipe(request,instance_id):
    if request.method == "POST":
        if request.user.is_authenticated:
            form_instance = forms.ReviewForm(request.POST)
            if form_instance.is_valid():
                new_reci = form_instance.save(request=request, reci_id=instance_id)
                return redirect("/view/"+str(instance_id))
        else:
            form_instance = forms.ReviewForm()
    else:
        form_instance = forms.ReviewForm()
            
    context = {
            "title":"Review",
            "opener":"Review Recipe",
            "add":"/add/",
            "review":"/review/",
            "view":"/view/",
            "login":"/login/",
            "logout":"/logout/",
            "reci_id":instance_id,
            "form":form_instance,
            }
    return render(request, "review.html", context=context)

def addIng(request, instance_id):
    if request.method == "POST":
        form_instance = forms.IngredientForm(request.POST)
        if(form_instance.is_valid()):
                form_instance.save(request=request, rec_id = instance_id)
                return redirect("/ingredient/" + str(instance_id)+"/")
    else:
        form_instance = forms.IngredientForm()
    context = {
            "rec_id":instance_id,
            "form":form_instance,
            "title":"Ingredients",
            "opener":"Add Ingredients",
            "add":"/add/",
            "login":"/login/",
            "logout":"/logout/",
        }

    return render(request, "ingredient.html", context=context)


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

def logout_view(request):
    logout(request)
    return redirect("/")

