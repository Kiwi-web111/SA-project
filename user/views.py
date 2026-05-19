from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CustomUserChangeForm, CustomUserCreationForm


@login_required
@user_passes_test(lambda u: u.is_superuser)
def user_management_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '使用者已成功新增。')
            return redirect('user-root')
    else:
        form = CustomUserCreationForm()

    return render(request, 'user/user_management.html', {
        'form': form,
    })


@login_required
@user_passes_test(lambda u: u.is_superuser)
def user_list_view(request):
    users = User.objects.all().order_by('username')
    return render(request, 'user/user_edit_list.html', {
        'users': users,
    })


@login_required
@user_passes_test(lambda u: u.is_superuser)
def user_edit_view(request, user_id):
    user_obj = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user_obj)
        if form.is_valid():
            form.save()
            messages.success(request, '使用者已成功更新。')
            return redirect('user-root')
    else:
        form = CustomUserChangeForm(instance=user_obj)

    return render(request, 'user/user_edit.html', {
        'form': form,
        'edit_user': user_obj,
    })


@login_required
@user_passes_test(lambda u: u.is_superuser)
def user_create_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '使用者已成功新增。')
            return redirect('user-create')
    else:
        form = CustomUserCreationForm()

    return render(request, 'user/user_form.html', {'form': form})


def user_login_view(request):
    if request.user.is_authenticated:
        return redirect('/')

    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('/')

    return render(request, 'user/login.html', {'form': form})


def user_logout_view(request):
    logout(request)
    return redirect('/')
