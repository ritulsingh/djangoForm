from django.shortcuts import render
from .models import Information
from .forms import MyForm

# Create your views here.

def my_form(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()  #Save form data to data base

            # Adding Form Data to list
            lst = []
            lst.append(request.POST['fullname']) 
            lst.append(request.POST['email'])
            lst.append(request.POST['mobile_number'])
            lst.append(request.POST['location'])
            lst.append(request.POST['company_name'])
            lst.append(request.POST['brand'])
            lst.append(request.POST['clint_type'])
            lst.append(request.POST['avg_Revenue'])
            return render(request, 'dataPrint.html', {"list": lst})
    else:
        form = MyForm()
    return render(request, 'index.html', {'form': form})