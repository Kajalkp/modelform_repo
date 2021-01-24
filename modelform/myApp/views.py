from django.shortcuts import render
from myApp.forms import StudentForm
# Create your views here.
def myView(request):
    f=StudentForm()
    if(request.method=="POST"):
        f=StudentForm(request.POST)
        if f.is_valid():
            f.save(commit=True)
            print("record is inserted succesfully")
    d={'form':f}
    return render(request,'myApp/1.html',d)
