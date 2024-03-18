from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm , UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.views import redirect_to_login



class UserAccessMixin(PermissionRequiredMixin):
    group_required = None  # Name of the required group
    redirect_url = 'dashboard/'  # Custom redirect URL

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect_to_login(request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())

        if self.group_required and not (request.user.is_superuser or request.user.groups.filter(name=self.group_required).exists()):
            return redirect(self.redirect_url)

        return super(UserAccessMixin, self).dispatch(request, *args, **kwargs)



@login_required
def BASE(request):
    return render(request, 'base.html', {})

# # Create your views here.
@login_required
def index(request):
    template = 'index.html'
    context = {}
    return render(request, template, context)


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # Assurez-vous de spécifier votre template si nécessaire

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Ajoutez vos variables de contexte personnalisées ici
        context['show_success_toast'] = True
        context['message_success'] = 'Authentification réussie'
        return context

def user_login(request):
    context = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    context = {'show_success_toast': True, 'message_success': 'Authentification réussie'}
                    return render(request, 'accounts/dashboard.html', context)
                else:
                    context = {'show_error_toast': True, 'message_error': 'Compte désactivé'}
                    return render(request, 'accounts/login.html', context)

            else:
                context = {'show_error_toast': True, 'message_error': 'Login invalide'}
                return render(request, 'accounts/login.html', context)
    else:
        form = LoginForm()
        context = {'form': form}
    print(context)
    return render(request, 'accounts/login.html', context)

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html', {'section': 'dashboard'})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'accounts/register_done.html', {'new_user': new_user})
        else:
            for field, errors in user_form.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        user_form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'user_form': user_form})

@login_required
def edit(request):
    context = {}
    user_form = UserEditForm(instance=request.user, data=request.POST)
    profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }     
    
    if request.method == 'POST':
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile mis à jour avec succès')
            context = {
                'user_form': user_form,
                'profile_form': profile_form,
            }
            return render(request, 'accounts/edit.html', context)

        else:
            messages.error(request, 'Erreur lors de la mise à jour de votre profil')

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }  
    return render(request, 'accounts/edit.html', context)

@login_required
def profile(request):
    context = {}
    user_form = UserEditForm(instance=request.user, data=request.POST)
    profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
    context = {
        'user_form': user_form,
        'profile_form': profile_form
        }
    if request.method == 'POST':
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile mis à jour avec succès')
            context = {
                'user_form': user_form,
                'profile_form': profile_form,
            }
            return render(request, 'accounts/profile.html', context)

        else:
            messages.error(request, 'Erreur lors de la mise à jour de votre profil')

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        } 

    return render(request, 'accounts/profile.html', context)


