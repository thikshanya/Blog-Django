from rest_framework import viewsets
from .models import Blog
from .serializers import BlogSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.Objects.all()
    serializer_class = BlogSerializer
    filter_backends =  [filters.DjangoFilterBackend]
    filterset_fields = ['title','categories','tags','content','is_draft']
    pagination_class = pagination.PageNumberPagination
    page_size = 5
