from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    recipeName = models.CharField(max_length=60)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    recipeDescription = models.CharField(max_length=500)
    foodImage = models.ImageField(
        max_length=144,
        upload_to='uploads/%Y/%m/%d/')
    foodCategories = (
        ('Asia', 'Asian'),# an example, first item is value stored in database
        ('Amer', 'American'),      #             second item is what is shown in the form's field
        ('Chin', 'Chinese'),
        ('Indi', 'Indian'),
        ('Ital', 'Italian'),
        ('Japa', 'Japanese'),
        ('Mexi', 'Mexican'),
        ('Thai', 'Thai'),
        ('', ''),
        ('Othe', 'Other'),
    )
    foodCategory = models.CharField(max_length=1, choices=foodCategories)#may have to change max_length from 1, look at models documentation
    recipeUrl = models.URLField(max_length=240,blank=True)
    recipeDirections =  models.CharField(max_length=240, blank=True)

    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.recipeName

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.CharField(max_length=500)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ratingOptions = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    rating = models.CharField(max_length=1, choices=ratingOptions)

    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username + " " + self.review

class Ingredient(models.Model):
    ingredient = models.CharField(max_length=60)
    amount = models.CharField(max_length=30)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.ingredient + " " + self.amount


