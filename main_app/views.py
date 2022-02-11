from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Bird, Seed
from .forms import FeedingForm

# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def birds_index(request):
    birds = Bird.objects.all()
    return render(request, 'birds/index.html', { 'birds': birds })

def birds_detail(request, bird_id):
    bird = Bird.objects.get(id=bird_id)
    feeding_form = FeedingForm()
    seed_ids = bird.seeds.all().values_list('id')
    seeds = Seed.objects.exclude(id__in=seed_ids)
    return render(request, 'birds/detail.html', { 
        'bird': bird, 
        'feeding_form': feeding_form, 
        'seeds': seeds 
    })

class BirdCreate(CreateView):
    model = Bird
    fields = ['name', 'breed', 'description', 'age']

class BirdUpdate(UpdateView):
    model = Bird
    fields = ['breed', 'description', 'age']

class BirdDelete(DeleteView):
    model = Bird
    success_url = '/birds/'

def add_feeding(request, bird_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.cat_id = bird_id
    new_feeding.save()
  return redirect('detail', bird_id=bird_id)

class SeedList(ListView):
    model = Seed

class SeedDetail(DetailView):
    model = Seed

class SeedCreate(CreateView):
    model = Seed
    fields = ['name']

class SeedUpdate(UpdateView):
    model = Seed
    fields = ['name']

class SeedDelete(DeleteView):
    model = Seed
    success_url = '/seeds/'

def assoc_seed(request, bird_id, seed_id):
    bird = Bird.objects.get(id=bird_id)
    bird.seeds.add(seed_id)
    return redirect('detail', bird_id=bird_id)

def unassoc_seed(request, bird_id, seed_id):
  bird = Bird.objects.get(id=bird_id)
  bird.seeds.remove(seed_id)
  return redirect('detail', bird_id=bird_id)