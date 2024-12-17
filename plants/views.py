from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, DetailView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Plant
from plants.forms import PlantForm


### the MainView lists all plants:
class MainView(LoginRequiredMixin, View):
    def get(self, request):
        plant_all=Plant.objects.all().order_by('-date_added') #newest at the top
        context={
            "plant_list":plant_all
        }
        return render(request, "plants/plant_list.html", context)


### view for individual plant detail page:
class PlantDetailView(LoginRequiredMixin, DetailView):  #class-based view - automatically handles the object retrieval, template rendering, and HTTP response creation
    model= Plant
    template_name = 'plants/plant_detail.html'
    context_object_name = 'plant' #use in template

# logout:
class OpenView(View):
    def get(self, request):
        return render(request, "plants/logout_view.html")

### CreateView for adding new plant:
class PlantCreateView(LoginRequiredMixin,View):
    def get(self, request):
        form = PlantForm()
        context = {"form":form}
        return render(request,"plants/plant_form.html", context)

    def post(self, request):
        # bind the form with POST data and files for image upload
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # redirect to a success page or to the plant list after successful submission
            return redirect('plants:plant_success')
        else:
            # If the form is not valid, re-render the form with error messages
            context = {"form": form}
            return render(request, "plants/plant_form.html", context)

# a view for the success page after adding a new plant:
class PlantSuccessView(LoginRequiredMixin,TemplateView):
    template_name = "plants/plant_success.html"

### Update view:
# UpdateView automatically uses POST method, no need to explicitly define (but need to specify in html template)
class PlantUpdateView(LoginRequiredMixin,UpdateView):
    model = Plant
    context_object_name = 'plant'
    template_name = "plants/plant_update.html"
    form_class = PlantForm
    success_url = reverse_lazy('plants:all')


### Delete view:
class PlantDeleteView(LoginRequiredMixin,DeleteView):
    model = Plant
    template_name = 'plants/plant_confirm_delete.html'
    context_object_name = 'plant'
    success_url = reverse_lazy('plants:all')




