from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm

# Create your views here.
def index(request):
    item_list = Item.objects.all()
    return render(request,'food/index.html',{'items': item_list})

def item(request):
    return HttpResponse('<h1>item Page</h1>')

def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    return render(request,'food/detail.html',{'item':item})

def create_item(request):
    form = ItemForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request,'food/item_form.html',{'form':form,'title':'Add New Item','button_text':'Add Item'})

def update_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None,request.FILES or None,instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/item_form.html',{'form':form,'title':'Update Item','button_text':'Update Item'})

def delete_item(request,id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    
    return render(request,'food/item_delete.html',{'item':item})