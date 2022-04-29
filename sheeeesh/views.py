from django.shortcuts import render, get_object_or_404
from .models import Item

# Create your views here.
def index(request):
    items = Item.objects.all()
    return render(request, 'sheeeesh/index.html', {'items': items})

def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        item = Item(name=name)
        item.save()
    return render(request, 'sheeeesh/create.html')

def update(request, id):
    item = get_object_or_404(Item, pk=id)
    if request.method == 'POST':
        item.name = request.POST['name']
        item.save()        
    return render(request, 'sheeeesh/update.html', {'item': item})

def delete(request, id):
    item = get_object_or_404(Item, pk=id)
    if request.method == 'POST':
        item.delete()