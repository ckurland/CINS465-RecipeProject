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


class IngredientForm(forms.Form):
    ingredientName = forms.CharField(label="Ingredient Name",max_length=60)
    amount = forms.CharField(label="Amount",max_length=30)

    def save(self, request, rec_id, commit=True):
        rec = models.Recipe.objects.get(id=rec_id)
        new_ing = models.Ingredient(
            ingredient=self.cleaned_data["ingredientName"],
            amount=self.cleaned_data["amount"],
            recipe=rec
            )
        if commit:
            new_ing.save()
        return new_ing

      
class ReviewForm(forms.Form):
    review = forms.CharField(label='Review', max_length=500)
    rating = forms.ChoiceField(label="Rating",choices=models.Review.ratingOptions)

    def save(self, request, reci_id, commit=True):
        reci_instance = models.Recipe.objects.get(id=reci_id)
        new_revi = models.Review(
            review=self.cleaned_data["review"],
            rating=self.cleaned_data["rating"],
            recipe=reci_instance,
            author=request.user
            )
        if commit:
            new_revi.save()
        return new_revi


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
