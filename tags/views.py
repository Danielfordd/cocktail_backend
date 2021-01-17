from django.shortcuts import render
from django.http import JsonResponse
from .models import CocktailTag


def load_tags(request):
    """
    Returns all available tags.
    """
    tags = [tag.tag for tag in CocktailTag.objects.all()]
    return JsonResponse({'tags': tags})
