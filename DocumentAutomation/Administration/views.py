from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.views.generic import ListView, View
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserUpdateForm


# Create your views here.
def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error': 'The username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('dashboard')


def create_account_view(request):
    if request.method == 'GET':
        return render(request, 'create-account.html', {
            'form': CustomUserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = CustomUser.objects.create_user(first_name=request.POST['first_name'],
                                                      last_name=request.POST['last_name'],
                                                      email=request.POST['email'],
                                                      username=request.POST['username'],
                                                      password=request.POST['password1'],
                                                      role=request.POST['role'])
                user.save()
                return redirect('dashboard')
            except IntegrityError:
                return render(request, 'create-account.html', {
                    'form': CustomUserCreationForm,
                    'error': f'User already exists'
                })
        return render(request, 'create-account.html', {
            'form': CustomUserCreationForm,
            'error': 'Passwords do not match'
        })


def logout_view(request):
    logout(request)
    return redirect('login')


class UserListView(ListView):
    model = CustomUser
    template_name = 'user-list.html'
    context_object_name = 'users'


class UserUpdateView(View):
    def get(self, request, pk):
        user = get_object_or_404(CustomUser, pk=pk)
        form = CustomUserUpdateForm(instance=user)
        return render(request, 'edit-user.html', {
            'form': form,
            'user': user
        })

    def post(self, request, pk):
        user = get_object_or_404(CustomUser, pk=pk)
        form = CustomUserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            new_password1 = form.cleaned_data.get('new_password1')
            if new_password1:
                user.set_password(new_password1)
            form.save()
            user.save()
            return redirect('login')
        else:
            return render(request, 'edit-user.html', {
                'form': form,
                'user': user
            })


class UserDeleteView(View):
    def get(self, request, pk):
        user = get_object_or_404(CustomUser, pk=pk)
        return render(request, 'user-confirm-delete.html', {
            'user': user
        })

    def post(self, request, pk):
        user = get_object_or_404(CustomUser, pk=pk)
        user.delete()
        return redirect('user-list')
