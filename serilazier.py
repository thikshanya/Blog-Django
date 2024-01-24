# 1. Create a rest endpoint that stores Blog Details, use categories and tags (there can be multiple tags) to organize posts for easy navigation and search.
# 2. Blog can be saved as draft
# 4. List all blogs - Implement pagination
# 2. Filter blogs using the categories and tags


from rest_framework import serializers
from .models import Blog,Catgory, Tags


class CategorySerializer(serializers,ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class TagsSerializer(serializers,ModelSerializer):
    class Meta:
        model = Tags 
        fields = ['name']

class BlogSerializer(serializers,ModelSerializer):
    categories = CategorySerializer(many=True)
    tags = TagsSerializer(many=True)

    class Meta:
        model = Blog
        fields = ['title','categories','tags','content','is_draft']

