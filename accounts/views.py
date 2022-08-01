from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserLoginForm, UserRegistrationForm, UserCreationForm, ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('core:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'You have successfully logged in!', 'success')
                return redirect('core:home')
            else:
                messages.error(request, 'Your email or password is incorrect!', 'danger')
        return render(request, self.template_name, {'form': form})


class UserRegistrationView(View):
    form_class = UserCreationForm
    template_name = 'accounts/register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('core:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['email'], cd['full_name'], cd['password2'])
            user.save()
            messages.success(request, 'You have successfully registered!', 'success')
            return redirect('accounts:login')

        messages.error(request, 'Oops! Something went wrong!', 'danger')
        return render(request, self.template_name, {'form': form})


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'You have successfully logged out!', 'success')
        return redirect('core:home')


class UserProfileView(LoginRequiredMixin, View):
    template_name = 'accounts/profile.html'

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        return render(request, self.template_name, {'user': user})


class VerifyEmailView(LoginRequiredMixin, View):
    pass


class SendVerifyCodeView(LoginRequiredMixin, View):
    pass


class ForgotPasswordView(LoginRequiredMixin, View):
    pass


class ResetPasswordView(LoginRequiredMixin, View):
    pass


class ChangePasswordView(LoginRequiredMixin, View):
    pass


class ChangeEmailView(LoginRequiredMixin, View):
    pass


class UserProfileEditView(LoginRequiredMixin, View):
    form_class = ProfileForm
    template_name = 'accounts/profile_edit.html'

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        form = self.form_class(instance=user.profile, initial={'email': user.email, 'full_name': user.full_name})
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        form = self.form_class(request.POST, instance=user.profile)
        if form.is_valid():
            form.save()
            request.user.email = form.cleaned_data['email']
            request.user.full_name = form.cleaned_data['full_name']
            request.user.save()
            messages.success(request, 'Your profile has been updated!', 'success')
            return redirect('accounts:profile', pk=pk)
        messages.error(request, 'Oops! Something went wrong!', 'danger')
        return render(request, self.template_name, {'form': form})




