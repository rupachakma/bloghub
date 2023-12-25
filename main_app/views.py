from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate,login,logout
from main_app.forms import BloggerProfileForm, LoginForm, PostForm,RegisterForm, UserProfileUpdateForm, ViewerProfileForm
from django.contrib.auth.decorators import login_required
from main_app.models import Blogpost, Viewer_Profile

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request,"register.html",{'form':form})

def loginpage(request):
    if request.method == "POST":
        
        form = LoginForm(request=request,data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                user_type = user.user_type
                if user_type == 'blogger':
                    return redirect("postlist")
                elif user_type == 'viewer':
                    return redirect("postlist")
                else:
                    return HttpResponse("Invalid User")
    else:
        form = LoginForm()
    return render(request,"login.html",{'form':form})

def logoutpage(request):
    logout(request)
    return redirect("login")

@login_required
def profile_page(request):  
        user = request.user
        if user.is_authenticated:
           
            if user.user_type == 'blogger':
                templates_name = "bloggers/profile.html"

            elif user.user_type == 'viewer':
                templates_name = "viewers/profile.html"
            else:
                return HttpResponse("Invalid User")
        else:
            return HttpResponse("User is not Authenticated")

        return render(request,templates_name)

@login_required
def post_list(request):
    posts = Blogpost.objects.all()
    return render(request,"postlist.html",{'posts':posts})

@login_required
def post_details(request,id):
    post = get_object_or_404(Blogpost, id=id)
    return render(request,"postdetails.html",{'post':post})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.blogger = request.user
            post.save()
            return redirect('postlist') 
    else:
        form = PostForm()

    return render(request, 'bloggers/create_post.html', {'form': form})

@login_required
def delete_post(request,id):
    post = get_object_or_404(Blogpost, id=id)

    if request.user == post.blogger:
        post.delete()
        return redirect('postlist')
    else:
        return redirect('postlist')

@login_required
def update_post(request, id):
    post = get_object_or_404(Blogpost, id=id)
    
    if request.user == post.blogger:
        if request.method == 'POST':
            form = PostForm(request.POST,request.FILES, instance=post)
            if form.is_valid():
                form.save()
                return redirect('postlist') 
        else:
            form = PostForm(instance=post)

        return render(request, 'bloggers/update_post.html', {'form': form})
    else:
        return redirect('postlist')
    

@login_required
def update_blogger_profile(request):
        user = request.user
        blogger_profile = user.blogger_profile

        if request.method == 'POST':
            user_form = UserProfileUpdateForm(request.POST, instance=user)
            blogger_profile_form = BloggerProfileForm(request.POST, request.FILES, instance=blogger_profile)

            if user_form.is_valid() and blogger_profile_form.is_valid():
                user_form.save()
                blogger_profile_form.save()

                # Redirect to the updated profile or another page
                return redirect('profile_view')
        else:
            user_form = UserProfileUpdateForm(instance=user)
            blogger_profile_form = BloggerProfileForm(instance=blogger_profile)

        return render(request, 'bloggers/update_profile.html', {'user_form': user_form, 'blogger_profile_form': blogger_profile_form})

def profile_view(request):
    user = request.user
    blogger_profile = user.blogger_profile

    context = {
        'user': user,
        'blogger_profile': blogger_profile,
    }

    return render(request, 'bloggers/profile.html', context)

@login_required
def update_viewer_profile(request):
    user = request.user

    if hasattr(user, 'viewer_profile'):
        viewer_profile = user.viewer_profile
    else:
        viewer_profile = Viewer_Profile(user_profile=user)
        viewer_profile.save()

    if request.method == 'POST':
        user_form = UserProfileUpdateForm(request.POST, instance=user)
        viewer_profile_form = ViewerProfileForm(request.POST, request.FILES, instance=viewer_profile)

        if user_form.is_valid() and viewer_profile_form.is_valid():
            user_form.save()
            viewer_profile_form.save()

            return redirect('viewer_profile_view')
    else:
        user_form = UserProfileUpdateForm(instance=user)
        viewer_profile_form = ViewerProfileForm(instance=viewer_profile)

    return render(request, 'viewers/update_profile.html', {'user_form': user_form, 'viewer_profile_form': viewer_profile_form})

def viewer_profile_view(request):
    user = request.user
    viewer_profile = user.viewer_profile

    context = {
        'user': user,
        'viewer_profile': viewer_profile,
    }

    return render(request, 'viewers/profile.html', context)