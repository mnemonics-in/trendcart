from django.shortcuts import render
from django.db.models import Q
from Product.models import Product

def search_results(request):
    query =""
    b = None
    if (request.method == "POST"):
        query = request.POST['S']
        if (query):
            productresult = Product.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query))
    return render(request, template_name= 'search_results.html', context={'query': query, 'results': productresult})
