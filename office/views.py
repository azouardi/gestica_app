from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator

from accounts.views import UserAccessMixin
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views import View
from .forms import *

# Create your views here.

class CompanyListView(LoginRequiredMixin, UserAccessMixin, View):
    model = Company
    template_name = 'office/company_list.html'
    context_object_name = 'company'
    permission_required = 'office.view_company'

    def get(self, request):
        search_query = request.GET.get('search_query', '')
        companies = self.model.objects.filter(
            Q(name__icontains=search_query) |
            Q(identifiant_fiscal__icontains=search_query) |
            Q(ice__icontains=search_query)|
            Q(rc__icontains=search_query)|
            Q(cnss__icontains=search_query)|
            Q(tp__icontains=search_query)
        )

        # Pagination
        paginator = Paginator(companies, 10)  # 15 companies per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
         
        context = {
            'page_obj': page_obj

        }
        print(companies)
        return render(request, self.template_name, context)


class CompanyCreateView(LoginRequiredMixin, UserAccessMixin, View):
    model = Company
    form_class = CompanyForm
    template_name = 'office/company_form.html'
    permission_required = 'office.add_company'

    def get(self, request):
        form = CompanyForm()
        context = {
            'form': form
        }
        print(form)
        return render(request, 'office/company_form.html', context)

    def post(self, request):
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Entreprise créée avec succès')
            return redirect('office:company_list')
        else:
            messages.error(request, form.errors)
            print(form.errors)
        context = {
            'form': form
        }
        return render(request, 'office/company_form.html', context)

class CompanyUpdateView(LoginRequiredMixin, UserAccessMixin, View):
    model = Company
    form_class = CompanyForm
    template_name = 'office/company_form.html'
    permission_required = 'office.change_company'

    def get(self, request, pk):
        company = Company.objects.get(id=pk)
        form = CompanyForm(instance=company)
        context = {
            'form': form
        }
        return render(request, 'office/company_form.html', context)

    def post(self, request, pk):
        company = Company.objects.get(id=pk)
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            # Vérifiez chaque case à cocher "Supprimer" et supprimez le fichier si nécessaire
            if form.cleaned_data.get('delete_logo'):
                company.logo.delete(save=False)
            if form.cleaned_data.get('delete_file_rc'):
                company.file_rc.delete(save=False)
            if form.cleaned_data.get('delete_file_if'):
                company.file_if.delete(save=False)
            form.save()
            messages.success(request, 'Entreprise modifiée avec succès')
            return redirect('office:company_list')
        context = {
            'form': form
        }
        return render(request, 'office/company_form.html', context)
    
class CompanyDeleteView(LoginRequiredMixin, UserAccessMixin, View):
    medel = Company
    template_name = 'office/company_delete.html'
    permission_required = 'office.delete_company'

    def get(self, request, pk):
        company = Company.objects.get(id=pk)
        context = {
            'company': company
        }
        return render(request, 'office/company_delete.html', context)

    def post(self, request, pk):
        company = Company.objects.get(id=pk)
        company.delete()
        messages.success(request, 'Entreprise supprimée avec succès')
        return redirect('office:company_list')
    
class CompanyDetailView(LoginRequiredMixin, UserAccessMixin, View):
    model = Company
    template_name = 'office/company_detail.html'
    permission_required = 'office.view_company'

    def get(self, request, pk):
        company = Company.objects.get(id=pk)
        context = {
            'company': company
        }
        return render(request, 'office/company_detail.html', context)

    
    