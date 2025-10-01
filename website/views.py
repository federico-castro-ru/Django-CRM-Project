from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.

def home(request):
    records = Record.objects.all()
    
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"You have been logged in as {username}.")
            return redirect('home')
        else:
            messages.success(request, "Log in unsuccessful.")
            return redirect('home')

    return render(request, 'home.html', {'records': records})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully signed up.")
            return redirect('home')
    
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})
    
    return render(request, 'signup.html', {'form': form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look up record
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You are not authorized to view this page.")
        
def delete_record(request, pk):
    if request.user.is_authenticated:
       record_to_delete = Record.objects.get(id=pk)
       record_to_delete.delete()
       messages.success(request, f"Record {record_to_delete.id} deleted successfully.")
       return redirect('home')
    
    else:
        messages.success(request, "You are not authorized to delete records.")
        return redirect('home')
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "You have added a new record.")
                return redirect('home')
        return render(request, 'add_record.html', {"form":form})
    else:
        messages.success(request, "You are not authorized to add new records.")
        return redirect('home')
    
def update_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None)
        return render(request, 'update_record.html', {'record':record})
    
    else:
        messages.success(request, "You are not authorized to update records.")
        return redirect('home')