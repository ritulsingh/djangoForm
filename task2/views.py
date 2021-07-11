from django.shortcuts import render
from numpy.core.fromnumeric import sometrue
from .models import Information
from .forms import MyForm
import matplotlib.pyplot as plt
import pandas as pd

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

def index(request):
    if "GET" == request.method:
        return render(request, 'fileUpload.html', {'something':False})
    else:
        excel_file = request.FILES["excel_file"]

        # you may put validations here to check extension or file size
        df = pd.read_excel(excel_file)

        # getting a particular sheet by name out of many sheets
        worksheet = df['ABC'].value_counts()
        excel = worksheet.to_dict()
        excel = dict(reversed(list(excel.items())))

        print(excel)
        print(type(excel))
        fig = plt.figure(figsize =(5, 5))
        plt.pie(excel.values(), labels = excel.keys())
        plt.legend(title = "ABC")
        plt.savefig('media/download.png',dpi=100)
        
        return render(request, 'fileUpload.html', {'dictionary': excel, 'something':True})