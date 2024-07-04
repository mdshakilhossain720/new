from django.shortcuts import render
from . forms import StudentRegestions

# Create your views here.

def StudentView(request):
    if request.method == 'POST':
        fm=StudentRegestions(request.POST)
        if fm.is_valid():
           fm.cleaned_data['name']
           fm.cleaned_data['email']
           
           return render(request,'success.html',{'nm':'name'})
        print(fm)
    
    else:
     fm=StudentRegestions()
     print('hi i am a get method')
    #fm.order_fields(field_order=['name','first_name','email',])

    return render(request,'regestion.html',{'form':fm})
