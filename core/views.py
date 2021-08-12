from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from .forms import AddForm, Form, CarForm, Car, UserRegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home (request):
    return render(request, 'index.html')

def registerUser (request):
    form = UserRegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
        else:
            form = UserRegisterForm()
    print(form)
    return render(request, 'register.html', {'form': form})

class TestForm(FormView):
    template_name = 'form.html'
    form_class = AddForm
    success_url = 'results'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class Results(ListView):
    template_name = 'results.html'
    context_object_name = 'forms'
    queryset = Form.objects.all()

class CarForm(FormView):
    template_name = 'car_form.html'
    form_class = CarForm
    success_url = 'car_results'

    def form_valid(self, car_form):
        car_form.save()
        return super().form_valid(car_form)

class CarResults(ListView):
    template_name = 'car_results.html'
    context_object_name = 'car_forms'
    queryset = Car.objects.all()