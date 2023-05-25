from django.shortcuts import render
from .models import Category, Recipe
from django.db.models import Count

def category_list(request):
    categories = Category.objects.all()
    category_data = []
    for category in categories:
        category_data.append({
            'name': category.name,
            'recipe_count': Recipe.objects.filter(category=category).count()
        })
    return render(request, 'category_list.html', {'categories': category_data})

def main(request):
    return render(request,'main.html',{
        'recipes':Recipe.objects.order_by('-id')[:5],
    })

