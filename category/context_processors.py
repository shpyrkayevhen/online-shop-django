from .models import Category


def menu_links(request):
    '''Return all categories.'''
    links = Category.objects.all()
    return dict(links=links)

# Add to settings.py into TEMPLATES[] 
