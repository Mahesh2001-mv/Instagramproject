from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Image
from django.contrib.auth.decorators import login_required

# Create your views here.
# def homepage(request):
#     return HttpResponse('Hi Darlings this is my post')
#     posts = Post.objects.all()
#     return render(request, 'posts/home.html', {"posts" : posts})

@login_required(login_url='login')
def upload(request):
    if request.method == 'POST':
        image = request.FILES['image']
        caption = request.POST['caption']
        Image.objects.create(
            image=image,            
            caption=caption,
            user_id = request.user.id
        )
        return redirect('upload')
    return render(request, 'posts/upload.html')
