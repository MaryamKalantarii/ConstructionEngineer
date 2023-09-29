from django.shortcuts import render,redirect
from .models import Blog,Comment,Reply
from .forms import CommentForm, ReplyForm
from django.contrib import messages
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.
def blog(request):
    blog= Blog.objects.filter(status=True)

        
    context={
            'blog': blog,
        }
    return render(request,'blog/blog.html',context=context)







def blog_detail(request ,id):
    # if request.GET.get('search'):
    #     serch = Blog.objects.filter(content__contains=request.GET.get('search'))
    if request.method == 'GET':
        blog = Blog.objects.get(id=id)
        reply = Reply.objects.filter(status=True)

        context ={
                "blog": blog,
                'reply' : reply,
            }
        return render(request,'blog/blog-details.html',context=context)
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
            cid = comment.which_course.id
            return redirect (f'/blog/blog-detail/{cid}')
        else:
            messages.add_message(request,messages.ERROR,'chete baba ba in data dadanet .... zereshk')
            return redirect (request.path_info)