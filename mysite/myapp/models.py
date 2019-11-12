from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""
class Suggestion(models.Model):
    recipeName = models.CharField(max_length=60)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    recipeDescription = models.CharField(max_length=240)
    foodImage = models.ImageField(
        max_length=144,
        upload_to='uploads/%Y/%m/%d/')
    foodCategories = (
        ('S', 'Small'),# an example, first item is value stored in database
        ('', ''),      #             second item is what is shown in the form's field
        ('', ''),
    )
    foodCategory = models.CharField(max_length=10, choices=foodCategories)#may have to change max_length to 1, look at models documentation
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.author.username + " " + self.suggestion
"""
