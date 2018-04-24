from django.shortcuts import render
from django.http import HttpResponse
from .models import Treasure


# Create your views here.
def index(request):
    # return HttpResponse('<h1>Hello Explorers</h1>')
    # name = 'Gold Nugget'
    # value = 1000.00
    # context = {
    #     'treasure_name': name,
    #     'treasure_val': value
    # }
    # return render(request, 'index.html', context)
    treasures = Treasure.objects.all()
    return render(request, 'index.html', {'treasures': treasures})

# class Treasure:
#     def __init__(self, name, value, material, location):
#         self.name = name
#         self.value = value
#         self.material = material
#         self.location = location
#
#
# treasures = [
#     Treasure('Gold Nugget', 500.00, 'gold', "Curly's Creek, NM"),
#     Treasure("Fool's Gold", 0, 'pyrite', "Fool's Falls, CO"),
#     Treasure('Coffee Can', 20.00, 'tin', 'Acme, CA')
# ]
