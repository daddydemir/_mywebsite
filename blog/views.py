from django.shortcuts import render
from .models import Users, Blogs
from .forms import AddUserForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404


def index(request):
    list_of_blog = Blogs.objects.all()
    return render(request, 'blog/index.html', {'list_of_blog': list_of_blog})

def get_users(request):
    users = Users.objects.all()
    return render(request, 'blog/users.html', {'users': users})
    
def get_user(request , pk):
    u1 = get_object_or_404(Users, pk=pk)
    return render(request , 'blog/user_detail.html' , {'u1': u1})

def add_user(request):
    if(request.method == 'POST'):
        form = AddUserForm(request.POST)
        if(form.is_valid()):
            post = form.save(commit=False)
            post.save()
            return redirect('users' , )
    else:
        form = AddUserForm()
    return render(request, 'blog/add_user.html' , {'form': form})


