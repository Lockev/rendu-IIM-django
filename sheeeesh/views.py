from django.shortcuts import render, get_object_or_404
from .models import Item
from .forms import ItemForm

# Create your views here.
def index(request):
    items = Item.objects.all()
    return render(request, 'sheeeesh/index.html', {'items': items})

def create(request):
    context = {}
    item_form_create = ItemForm(request.POST or None)
    if item_form_create.is_valid():
        item_form_create.save()
        return render(request, 'sheeeesh/update.html', {'item': item_form_create})

    context["item"] = item_form_create
    return render(request, 'sheeeesh/create.html', context)

def update(request, id):
    context = {}
    item = get_object_or_404(Item, pk=id)
    item_form_update = ItemForm(request.POST or None, instance=item)
    if item_form_update.is_valid():
        item_form_update.save()  
            
    context["item"] = item_form_update
    return render(request, 'sheeeesh/update.html', context)

def delete(request, id):
    item = get_object_or_404(Item, pk=id)
    if request.method == 'POST':
        item.delete()