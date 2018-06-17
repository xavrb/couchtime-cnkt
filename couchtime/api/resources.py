from tastypie.resources import ModelResource
from api.models import movie

class MovieResource(ModelResource):
    class Meta:
        queryset = movie.objects.all()
        resource_name = 'movie'
