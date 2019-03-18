from django.shortcuts import render
from myfile.forms import RegistrationForm
def kinomir(request):
    form = RegistrationForm(request.POST or None )
    if request.method == "POST" and form.is_valid():
        print(form.cleaned_data)
        new_form = form.save()
    return render(request,'kinomir/kinomir.html', locals())
