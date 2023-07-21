from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Coffee, Maker



# Home page
def home(request):
    return render(request, 'home.html')

# About page
def about(request):
    return render(request, 'about.html')

# Coffee index
def coffee_index(request):
    return render(request, 'coffee/coffee_index.html', {
        'coffee': Coffee.objects.all()
    })

# Coffee detail
def coffee_detail(request, coffee_id):
    coffee = Coffee.objects.get(id=coffee_id)
    return render(request, 'coffee/coffee_detail.html', {
        'coffee': coffee
    })

# Maker index
def maker_index(request):
    return render(request, 'maker/maker_index.html', {
        'maker': Maker.objects.all()
    })

# Maker detail
def maker_detail(request, maker_id):
    maker = Maker.objects.get(id=maker_id)
    return render(request, 'maker/maker_detail.html', {
        'maker': maker
    })

# Create coffee
class CoffeeCreate(CreateView):
    model = Coffee
    fields = '__all__'

# Update coffee
class CoffeeUpdate(UpdateView):
    model = Coffee
    fields = '__all__'

# Delete coffee
class CoffeeDelete(DeleteView):
    model = Coffee
    success_url = '/coffee'

# Create maker
class MakerCreate(CreateView):
    model = Maker
    fields = '__all__'

# Update maker
class MakerUpdate(UpdateView):
    model = Maker
    fields = '__all__'

# Delete maker
class MakerDelete(DeleteView):
    model = Maker
    success_url = '/maker'

    