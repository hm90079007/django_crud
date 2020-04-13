from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    form = UserCreationForm()
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, 'account/signup.html',{'form':form })


#'from'がsingup.html の{{form}}
