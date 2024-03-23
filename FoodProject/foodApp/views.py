from django.forms import BaseModelForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.views import generic

def index(request):
    item_list = Item.objects.all()
    return render(request,'foodApp/index.html',{'item_list':item_list})

class IndexView(generic.ListView):
    model = Item
    template_name = 'foodApp/index.html'
    context_object_name = 'item_list'

def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context = {'item':item}
    return render(request,'foodApp/detail.html', context)

class ItemDetail(generic.DeleteView):
    model = Item
    template_name = 'foodApp/detail.html'

def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('foodApp:index')
            # return HttpResponse("Item added Successfully")
        
    form = ItemForm()
    return render(request, 'foodApp/create.html',{'form':form})

class CreateItem(generic.edit.CreateView):
    model = Item
    fields = ['item_name','item_desc','item_price','item_image']
    template_name = 'foodApp/create.html'

    def form_invalid(self,form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)

def update_item(request,id):
    item = Item.objects.get(id=id)
    form  = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('foodApp:index')
    return render(request,'foodApp/create.html',{'form':form, 'item':item})

def delete_item(request,id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('foodApp:index')
    return render(request,'foodApp/delete.html',{'item':item})

