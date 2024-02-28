from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Users,CartItem,WishlistItem,Feedback
# Create your views here.

def home(request):
    return render(request,'home-page.html')

@login_required(login_url="/signup")
def product(request):
    return render(request,'product-page.html')



@login_required(login_url="/signup")
def chair(request):
    if request.method == 'POST':
        if request.POST.get('action') == 'wishlist':
            if WishlistItem.objects.filter(user = request.user,title=request.POST.get('title'),price=request.POST.get('price'),image=request.POST.get('image')).exists():
                pass
            else:
                WishlistItem.objects.create(user = request.user,title=request.POST.get('title'),price=request.POST.get('price'),image=request.POST.get('image'))
        else:
            if CartItem.objects.filter(user = request.user,title=request.POST.get('title'),price=request.POST.get('price'),image=request.POST.get('image')).exists():
                pass
            else:
                CartItem.objects.create(user = request.user,title=request.POST.get('title'),price=request.POST.get('price'),image=request.POST.get('image'))
    return render(request,'chair-page.html')

@login_required(login_url="/signup")
def table(request):
    if request.method == 'POST':
        if request.POST.get('action') == 'wishlist':
            if WishlistItem.objects.filter(user = request.user,title=request.POST.get('title'),price=request.POST.get('price'),image=request.POST.get('image')).exists():
                pass
            else:
                WishlistItem.objects.create(user = request.user,title=request.POST.get('title'),price=request.POST.get('price'),image=request.POST.get('image'))
        else:
            if CartItem.objects.filter(user = request.user,title=request.POST.get('title'),price=request.POST.get('price'),image=request.POST.get('image')).exists():
                pass
            else:
                CartItem.objects.create(user = request.user,title=request.POST.get('title'),price=request.POST.get('price'),image=request.POST.get('image'))
    return render(request,'table-page.html')

@login_required(login_url="/signup")
def bed(request):
    if request.method == 'POST':
        if request.POST.get('action') == 'wishlist':
            if WishlistItem.objects.filter(user = request.user,title=request.POST.get('title'),price=request.POST.get('price'),image=request.POST.get('image')).exists():
                pass
            else:
                WishlistItem.objects.create(user = request.user,title=request.POST.get('title'),price=request.POST.get('price'),image=request.POST.get('image'))
        else:
            if CartItem.objects.filter(user = request.user,title=request.POST.get('title'),price=request.POST.get('price'),image=request.POST.get('image')).exists():
                pass
            else:
                CartItem.objects.create(user = request.user,title=request.POST.get('title'),price=request.POST.get('price'),image=request.POST.get('image'))
    return render(request,'bed-page.html')

@login_required(login_url="/signup")
def sofa(request):
    if request.method == 'POST':
        if request.POST.get('action') == 'wishlist':
            if WishlistItem.objects.filter(user = request.user,title=request.POST.get('title'),price=request.POST.get('price'),image=request.POST.get('image')).exists():
                pass
            else:
                WishlistItem.objects.create(user = request.user,title=request.POST.get('title'),price=request.POST.get('price'),image=request.POST.get('image'))
        else:
            if CartItem.objects.filter(user = request.user,title=request.POST.get('title'),price=request.POST.get('price'),image=request.POST.get('image')).exists():
                pass
            else:
                CartItem.objects.create(user = request.user,title=request.POST.get('title'),price=request.POST.get('price'),image=request.POST.get('image'))
    return render(request,'sofa-page.html')

@login_required(login_url="/signup")
def cupboard(request):
    if request.method == 'POST':
        if request.POST.get('action') == 'wishlist':
            if WishlistItem.objects.filter(user = request.user,title=request.POST.get('title'),price=request.POST.get('price'),image=request.POST.get('image')).exists():
                pass
            else:
                WishlistItem.objects.create(user = request.user,title=request.POST.get('title'),price=request.POST.get('price'),image=request.POST.get('image'))
        else:
            if CartItem.objects.filter(user = request.user,title=request.POST.get('title'),price=request.POST.get('price'),image=request.POST.get('image')).exists():
                pass
            else:
                CartItem.objects.create(user = request.user,title=request.POST.get('title'),price=request.POST.get('price'),image=request.POST.get('image'))
    return render(request,'cupboard-page.html')


def loginUser(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            return redirect('login-page')
    else:
        return render(request, 'Auth/login.html')
    
def logoutUser(request):
    logout(request)
    return redirect('home-page')

def signUpUser(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        if Users.objects.filter(email=email).exists():
            return redirect('signup-page')
        if password != re_password:
            return redirect('signup-page')
        user = Users(full_name=full_name, email=email, password=password,username=email)
        user.save()
        return redirect('login-page')
    else:
        return render(request,'Auth/signup.html')
    
@login_required(login_url="/signup")
def cart(request):
    carts = CartItem.objects.filter(user=request.user)
    return render(request,'cart.html',context={'carts':carts})

@login_required(login_url="/signup")
def wishlist(request):
    carts = WishlistItem.objects.filter(user=request.user)
    return render(request,'wishlist.html',context={'carts':carts})


def about(request):
    return render(request,'about.html')


def feedBack(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        feed = request.POST.get('feedback')
        Feedback.objects.create(name=name, email=email,feedback=feed)
        return redirect('home-page')
    return render(request,'feedback.html')


def contact(request):
    return render(request,'contact.html')