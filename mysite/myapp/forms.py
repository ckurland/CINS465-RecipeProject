from django import forms
from django.core.validators import validate_slug
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . import models


class RecipeForm(forms.Form):
    recipeName = forms.CharField(label="Recipe Name",max_length=60)
    recipeDescription = forms.CharField(label="Description",max_length=500)
    foodImage = forms.ImageField(label="Food Image")
    foodCategory = forms.ChoiceField(label="Category",choices=models.Recipe.foodCategories)
    recipeUrl = forms.URLField(label="URL (Optional)",max_length=240,required=False)
    recipeDirections = forms.CharField(label="Directions (Optional)",max_length=240,required=False)

    def save(self, request, commit=True):
        new_rec = models.Recipe(
            recipeName=self.cleaned_data["recipeName"],
            recipeDescription=self.cleaned_data["recipeDescription"],
            foodImage=self.cleaned_data["foodImage"],
            foodCategory=self.cleaned_data["foodCategory"],
            recipeUrl=self.cleaned_data["recipeUrl"],
            recipeDirections=self.cleaned_data["recipeDirections"],
            author=request.user
        )
        if commit:
            new_rec.save()
        return new_rec


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True
        )

    class Meta:
        model = User
        fields = ("username", "email",
                  "password1", "password2")

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
