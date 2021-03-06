
# /lists/views.py

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.shortcuts import render

from lists.forms import ExistingListItemForm
from lists.forms import ItemForm
# from lists.forms import NewListForm
from lists.models import List


User = get_user_model()

def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})

def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List()
        if request.user.is_authenticated():
            list_.owner = request.user
        list_.save()
        form.save(for_list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {"form": form})

def view_list(request, pk):
    list_ = List.objects.get(id=pk)
    form = ExistingListItemForm(for_list=list_)
    if request.method == 'POST':
        form = ExistingListItemForm(for_list=list_, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_)
    return render(request, 'list.html', {'list': list_, "form": form})

def my_lists(request, email):
    owner = User.objects.get(email=email)
    return render(request, 'my_lists.html', {'owner': owner})

def share_list(request, pk):
    list_ = List.objects.get(id=pk)
    list_.shared_with.add(request.POST['email'])
    return redirect(list_)
