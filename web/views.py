from django.shortcuts import render 
from django.http import HttpResponse  
from .models import posts
from django.views.generic.list import ListView 
from django.views.generic.edit import CreateView 
from django.views.generic.detail import DetailView 
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm 
from django.contrib.auth.models import User 
from django.urls import reverse_lazy 
from django.views.generic.edit import UpdateView, DeleteView, FormView 
from django.contrib.auth.views import LoginView  
from django.contrib.auth import login

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def index(request):
    return render(request, 'web/index.html') 


def sign_in(request):
    return render(request, "web/sign_in.html") 

class Post(ListView): 
    model=posts 
    context_object_name='post' 
    template_name='web/posts.html'   

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs) 
        context['post']=context["post"].filter(user=self.request.user) 
        search_input=self.request.GET.get('search-area') or '' 
        if search_input:
            context["post"]=context["post"].filter(title__icontains=search_input)
        return context



class AddPost(LoginRequiredMixin,CreateView):
    model=posts  
    fields=["title","headline","full_story", "post_id","image"]
    template_name="web/add_post.html"  
    success_url=reverse_lazy('add_post')  

    def form_valid(self, form): 
        form.instance.user=self.request.user 
        return super(AddPost, self).form_valid(form)


class ViewPost(DetailView):
    model=posts  
    context_object_name='post'
    template_name="web/post_details.html"   

class Registration(FormView):
    template_name="web/register.html" 
    form_class=UserCreationForm 
    redirect_authenticated_users=True 
    success_url=reverse_lazy('Index')  

    def form_valid(self, form): 
        user=form.save()
        if user is not None:
            login(self.request, user)
        return super(Registration, self).form_valid(form)

class EditPost(LoginRequiredMixin,UpdateView):
    model=posts 
    fields=["title","image","headline","full_story", "post_id"] 
    success_url=reverse_lazy("posts") 

class DeletePost(LoginRequiredMixin,DeleteView):
    model=posts 
    fields="__all__" 
    success_url=reverse_lazy("posts") 

class Login(LoginView):
    template_name='web/login.html' 
    fields='__all__' 
    redirect_authenticated_user=True 

    def get_success_url(self):
        return reverse_lazy("posts") 

