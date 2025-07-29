from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.
def index(request):
    item_list = Item.objects.all()
    return render(request,'food/index.html',{'items': item_list})

def item(request):
    return HttpResponse('<h1>item Page</h1>')

def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    return render(request,'food/detail.html',{'item':item})
