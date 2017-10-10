from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,Category
import markdown
from comments.forms import CommentForm
from django.shortcuts import render, get_object_or_404
def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    # cate_name = Category.objects.all().order_by('-id')
    # print(cate_name)
    return render(request,'blog/index.html',context= {'post_list':post_list})


def detail(request,pk):
    post = get_object_or_404(Post,pk = pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {
        'post':post,
        'form':form,
        'comment_list':comment_list
    }
    return render(request,'blog/detail.html',context=context)

def details(request,id):
    id = id
    pages = Post.objects.get(id = id)
    # print(pages)
    return render(request,'blog/detail.html',context={'post':pages})

# def category(request,id):
#     id = id
#     print(id)
#     category = Category.objects.filter(id=id)[0]
#     cate = category.post_set.all()
#     print(cate)
#     return render(request,'blog/index.html',context={'post_list':cate})
# # guidang
def archives(request,year,month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')

    return render(request, 'blog/index.html', context={'post_list': post_list})
#
def category(request,pk):
    cate = get_object_or_404(Category,pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})