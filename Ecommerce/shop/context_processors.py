from shop.models import Catergory


def menu_links(request):
    c=Catergory.objects.all()
    return{'links':c}