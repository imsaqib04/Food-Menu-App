from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Item
from django.template import loader
from django.shortcuts import redirect
from .forms import ItemForm

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

# Create your views here.

# function based
def index(request):
    item_list = Item.objects.all()

    context = {
        'item_list':item_list,
    }
    return render(request,'food/index.html',context)

# class Based 
class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name='item_list'


def item(request):
    return HttpResponse("Hello Saqib, This is a item !")

# function based
def details(request,item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item':item,
    }
    return render(request,'food/detail.html',context)

# class Based
class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'


# # function based
# def create_item(request):
#     form = ItemForm(request.POST or None)

#     if form.is_valid():
#         form.save()
#         return redirect("food.index")
    
#     return render(request,'food/item-form.html',{'form':form})


# #class Baased
# class CreateItem(CreateView):
#     model = Item
#     fields = ['item_name','item_desc','item_price','item_image']
#     template_name = 'food/item-form.html'

#     def form_valid(self,form):
#         form.instance.user_name = self.request.user

#         return super().form_valid(form)

#class Baased
class CreateItem(LoginRequiredMixin, CreateView):
    model = Item
    fields = ['item_name','item_desc','item_price','item_image']
    template_name = 'food/item-form.html'

    def form_valid(self,form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)


def update_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None,instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request,'food/item-form.html',{'form':form,'item':item})

# def delete_item(request,id):
#     item = Item.objects.get(id = id)

#     if request.method == 'POST':
#         item.delete()
#         return redirect("food:index")
    
#     return render(request,"food/item-delete.html",{'item':item})


def delete_item(request,id):
    item = get_object_or_404(Item, pk=id)

    # Check if the current user is the owner of the item or a superuser
    if request.user == item.user_name or request.user.is_superuser:
        if request.method == 'POST':
            item.delete()
            messages.success(request, 'Item deleted successfully.')
            return redirect('food:index')
        # For a GET request, render the confirmation page
        return render(request, 'food/delete_confirm.html', {'item': item})
    else:
        # If the user is not the owner, redirect them with an error message
        messages.error(request, 'You are not authorized to delete this item.')
        return redirect('food:index')