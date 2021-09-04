from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .register import ProfileUpdateForm, RegisterForm, UserUpdateForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('usersapp:login')
            
    else:
        form = RegisterForm()
    return render(request, 'usersapp/register.html', {'form': form})


@login_required
def user_profile(request, template_name='usersapp/profile.html'):
    if request.method == 'POST':
        update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if update_form.is_valid() & profile_form.is_valid():
            update_form.save()
            profile_form.save()
            messages.success(request, 'Your Account has bee updated!')
            return redirect('usersapp:user_profile')
    else:
        update_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'update_form': update_form, 'profile_form': profile_form
    }
    return render(request, template_name, context)
