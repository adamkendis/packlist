from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import ItemForm

def gear_list(request):
	items = Item.objects.all().order_by('weight_oz')
	return render(request, 'gear/gear_list.html', {'items': items, 'count': items.count()})

def gear_detail(request, pk):
	item = get_object_or_404(Item, pk=pk)
	return render(request, 'gear/gear_detail.html', {'item': item})

def gear_delete(request, pk):
	item = get_object_or_404(Item, pk=pk)
	item.delete()
	return redirect('/')

def gear_new(request):
	if request.method == 'POST':
		form = ItemForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = ItemForm()
	return render(request, 'gear/gear_edit.html', {'form': form})

def gear_edit(request, pk):
	item = get_object_or_404(Item, pk=pk)
	if request.method == 'POST':
		form = ItemForm(request.POST, instance=item)
		if form.is_valid():
			form.save()
			return redirect('/item/' + str(item.pk))
	else:
		form = ItemForm(instance=item)
	return render(request, 'gear/gear_edit.html', {'form': form})
