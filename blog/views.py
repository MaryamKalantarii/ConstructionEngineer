from django.shortcuts import render,redirect,get_object_or_404,redirect
from .models import Blog,Comment,Reply
from .forms import CommentForm, ReplyForm
from django.contrib import messages
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from projects.models import Category

# Create your views here.
def blog(request):
    if request.method =="GET":
        category = Category.objects.all()
        blog= Blog.objects.filter(status=True)
    elif request.GET.get('search'):
        blog = Blog.objects.filter(content__contains=request.GET.get('search'))
    blog = Paginator(blog,3)
    first_page = 1
    last_page = blog.num_pages
    try:
        page_number = request.GET.get('page')
        blog = blog.get_page(page_number)
    except EmptyPage:
        blog = blog.get_page(1)
    except PageNotAnInteger:
            blog = blog.get_page(1)
    context={
            'blog':blog,
            'first_page': first_page,
            'last_page': last_page,
            'category': category,
            }
    return render(request,'blog/blog.html',context=context)







def blog_detail(request ,id):
    if request.method == 'GET':
        try:
            comments = Comment.objects.filter(which_blog=id, status=True)
            blog = Blog.objects.get(id=id)
            reply = Reply.objects.filter(status=True)
            category = Category.objects.all()

            context ={
                'comments': comments,
                "blog": blog,
                'reply' : reply,
                'category': category,
                }
            return render(request,'blog/blog-details.html',context=context)
        except:
                return render(request,'blog/404.html')
    elif request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request,messages.SUCCESS,'نظر شما ارسال و به زودی منتشر می شود')
                return redirect (request.path_info)

            else:
                messages.add_message(request,messages.ERROR,'yor comment data is not valid')
                return redirect (request.path_info)




def reply(request, id):
    comment = Comment.objects.get(id=id)
    if request.method == 'GET':
        form = ReplyForm()

        context = {
            'comment' : comment,
            'form' : form,
        }
        return render(request,'blog/reply.html',context=context)
    
    elif request.method == 'POST' :
        form = ReplyForm(request.POST)
        if form.is_valid():
            form.save()
            cid = comment.which_blog.id
            return redirect (f'/blog/blog-detail/{cid}')
        else:
            messages.add_message(request,messages.ERROR,'chete baba ba in data dadanet .... zereshk')
            return redirect (request.path_info)

