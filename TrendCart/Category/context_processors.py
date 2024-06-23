from Category.models import Maincategory

def menu_links(request):
    c=Maincategory.objects.all()
    return {'links':c}