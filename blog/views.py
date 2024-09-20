from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
from .models import Post, Contact, AboutUs
from .forms import ContactForm
import logging

# posts = [
#     {'id': 1, 'title':'post 1', 'content':'content of post 1'},
#     {'id': 2, 'title':'post 2', 'content':'content of post 2'},
#     {'id': 3, 'title':'post 3', 'content':'content of post 3'},
#     {'id': 4, 'title':'post 4', 'content':'content of post 4'},
# ]

def home(request):
    title = "Latest Post"
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "blog/index.html", {'title': title, 'page_obj':page_obj})
    
def detail(request, slug):
    title = "Detail Post"
    
    try:
        post = Post.objects.get(slug=slug)
        related_posts = Post.objects.filter(category = post.category)
    except Post.DoesNotExist:
        raise Http404("Post does not")
    
    # post = next((item for item in posts if item['id'] == int(post_id)), None)
    # logger = logging.getLogger("TESTING")
    # logger.debug(f"Post is {post}") 
    return render(request, "blog/detail.html", {'title': title, 'post':post, 'related_posts':related_posts})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        logger = logging.getLogger("TESTING")
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            contact = Contact(name=name, email=email, message=message)
            contact.save()
            print(f"Name: {name}, Email: {email}, Message: {message}")
            success_message = 'Your Form has been submitted!'
            return render(request,'blog/contact.html', {'form':form,'success_message':success_message})
        else:
            logger.debug('Form validation failure')
        return render(request,'blog/contact.html', {'form':form, 'name': name, 'email':email, 'message': message})
    return render(request,'blog/contact.html')

def about(request):
    about_content = AboutUs.objects.first().content
    return render(request,'blog/about.html',{'about_content':about_content})
