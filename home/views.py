from django.shortcuts import render
from .models import Stock
from .forms import StockCreateForm, StockSearchForm, StockUpdateForm
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    title = "MTM-StockPile : Easy Inventory Management System"
    context = {
        "title": title,
    }
    return render(request, 'home.html', context)


def list_items(request):
    header = "LIST OF ITEMS"
    form = StockSearchForm(request.POST or None)
    queryset = Stock.objects.all()
    context = {
        "header": header,
        "queryset": queryset,
        "form": form,
    }
    if request.method == 'POST':
        queryset = Stock.objects.filter(category__icontains=form['category'].value(),
                                        item_name__icontains=form['item_name'].value())
        context = {
            "form": form,
            "header": header,
            "queryset": queryset,
        }
    return render(request, 'list_items.html', context)


def add_items(request):
    form = StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/list_items')
    context = {
        "form": form,
        "title": "Add Item",
    }
    return render(request, "add_items.html", context)


def update_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = StockUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = StockUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/list_items')

    context = {
        'form': form
    }
    return render(request, 'add_items.html', context)
