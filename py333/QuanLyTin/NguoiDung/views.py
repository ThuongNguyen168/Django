from django.shortcuts import render
from .models import Post
from .forms import RegistrationForm
from django.http import HttpResponseRedirect 

def index(request):
    return render(request, 'Page/index.html')

def DSBaiViet(request):
   	data = {
		'Posts': Post.objects.all(), 
   	}
   	return render(request, 'page/DSBaiViet.html', data)

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'Page/DangKy.html', {'form': form})

def loginn(request):
    return render(request, 'Page/login.html')