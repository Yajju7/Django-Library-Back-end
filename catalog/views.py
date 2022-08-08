from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from . models import *
from django.views.generic import CreateView,DetailView,ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def index(request):
    num_books = Book.objects.all().count()
    num_instances = bookInstance.objects.all().count()
    num_instances_avail = bookInstance.objects.filter(status__exact='a').count()
    
    context ={
        'num_books':num_books,
        'num_instances':num_instances,
        'num_instances_avail':num_instances_avail 
        
    }
    return render(request, 'catalog/index.html', context=context)

class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    fields = '__all__'
    
class BookDetail(DetailView):
    model = 'Book'

@login_required 
def my_view(request):
    return render(request, 'catalog/my_view.html')


class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'catalog/signup.html'
    
class CheckOutBooksByUserView(ListView, LoginRequiredMixin):
    model = bookInstance
    template_name = 'catalog/profile.httml'
    paginate_by: 5
    
    def get_queryset(self):
        return bookInstance.objects.filter(borrower = self.request.user)
    