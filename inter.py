# 1. Create a rest endpoint that stores Blog Details, use categories and tags (there can be multiple tags) to organize posts for easy navigation and search.
# 2. Blog can be saved as draft
# 4. List all blogs - Implement pagination
# 2. Filter blogs using the categories and tags

import django.db import model 

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Tags(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
class Blog(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextFields()
    catergories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tags)
    is_draft = models.ManyToManyField()


    def __str__(self):
        return self.title
        




