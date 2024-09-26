from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import MyLoginForm, UserRegisterForm, PostAddForm, PostEditForm
from .models import Post

# Create your views here.


# def index(request):
#     return render(request, template_name='posts.html')

#define a new view

def register(request):
    if request.method=='POST':
        user_req_form = UserRegisterForm(request.POST)
        if user_req_form.is_valid():
            new_user = user_req_form.save(commit=False)
            new_user.set_password(user_req_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/register_done.html',{'user_req_form':user_req_form})
    else:
        user_req_form = UserRegisterForm()

    return render(request, 'account/register.html',{'user_req_form':user_req_form})



def custom_logout(request):
    logout(request)
    # Redirect to a custom URL after logout, replace 'home_path' with your desired URL
    return render(request, 'registration/logged_out.html')

def posts_list(request):
    searchTerm = request.GET.get('searchpost')
    if searchTerm:
        posts_list = Post.objects.filter(post_title__icontains=searchTerm)
    else:
        posts_list = Post.objects.all()

    paginator = Paginator(posts_list, 1)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'posts.html',{'searchTerm':searchTerm,'posts_list':posts,'page':page})

def post_details_view(request, passed_id):
    print("helloooooo")
    #get the post with id value in the table as passed_id from url
    post_details = get_object_or_404(Post, id=passed_id)
    return render(request, 'postdetails.html', {'post_details': post_details})

def user_login(request):
    print(request.method)
    if request.method == 'POST':
        # we will be getting username and password through post
        login_form = MyLoginForm(request.POST)
        if login_form.is_valid():
            cleaned_data = login_form.cleaned_data
            auth_user = authenticate(request,
                                     username=cleaned_data['username'],
                                     password=cleaned_data['password'])

            if auth_user is not None:
                login(request, auth_user)
                return HttpResponse('Authenticated')
            else:
                return HttpResponse('Not Authenticated')

    else:
        login_form = MyLoginForm()
    return render(request, 'useraccount/login_form.html',{'login_form':login_form})
@login_required
def add_post(request):
    add_post_form = PostAddForm(request.POST, request.FILES)
    if request.method == 'POST':
        if add_post_form.is_valid():
            new_post = add_post_form.save(commit=False)
            new_post.post_author = request.user
            new_post.save()
            return redirect('home_path')
        else:
            add_post_form = PostAddForm()
    return render(request, 'account/add_post.html', {'add_post_form':add_post_form})

@login_required
def edit_post(request, passed_id):
    post_details = get_object_or_404(Post, id=passed_id)
    edit_post_form = PostEditForm(request.POST or None, request.FILES or None, instance=post_details)

    if edit_post_form.is_valid():
        edit_post_form.save()
        return redirect('home_path')

    return render(request, 'account/edit_post.html',{'edit_post_form': edit_post_form})