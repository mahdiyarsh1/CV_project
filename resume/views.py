import re
from .models import ContactMessage
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.conf import settings
import os
from django.shortcuts import redirect, render, HttpResponse
from .models import Post, CommentPost
from django.core.paginator import Paginator, InvalidPage
from .forms import Comment
# from .forms import ContactForm
# Create your views here.


# def comment(request, id):
#     print(request.method)
#     if request.method == "POST":
#         form = Comment(request.POST)
#         if form.is_valid():
#             post = Post.objects.get(id=id)
#             c_f = form.cleaned_data
#             comment = CommentPost.objects.create(
#                 comment_post=post, name=c_f.get("name"), comment_text=c_f.get("text")
#             )
#             print(c_f)
#     else:
#         form = Comment()
#     return redirect(f"{request.get_host()}/blog/{id}")
# ----------------------------------------------------------------------------------------------
# IN METHOD BE FUNCTION post_details MONTAGHEL SHOD


def index(request):
    return render(request=request, template_name='index.html')


def blog(request):
    return render(request=request, template_name="blog_1.html")


def download_resume(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'cv.pdf')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="cv.pdf"'
            return response
    raise Http404


# def contact_view(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')
#         ContactMessage.objects.create(
#             name=name, email=email, subject=subject, message=message)
#         return redirect('success')

#     return render(request, 'index.html')


# def success_view(request):
#     return render(request, 'success.html')


def show_bamdad(request):
    return render(request=request, template_name='detail_page_bamdad.html')


def show_cs50x(request):
    return render(request=request, template_name='detail_page_cs50x.html')


def show_cando(request):
    return render(request=request, template_name='detail_page_cando.html')


# def index_view(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')

#         # ذخیره کردن اطلاعات فرم در دیتابیس
#         ContactMessage.objects.create(
#             name=name, email=email, subject=subject, message=message)

#         return redirect('success_url')  # تغییر به URL صفحه موفقیت

#     return render(request, 'index.html')


# def success_view(request):
#     return render(request, 'success.html')


#     posts = Post.objects.all()
#     paginator = Paginator(posts, 2)
#     page = request.GET.get("page", 1)
#     try:
#         result = paginator.page(page)
#         print(paginator.num_pages)
#     except InvalidPage:
#         result = paginator.page(1)

#     return render(
#         request=request,
#         template_name="index.html",
#         context={"posts": posts, "result": result},
#     )


# def post_details(request, id):
#     if request.method == "POST":
#         form = Comment2(request.POST)
#         if form.is_valid():
#             form.save()
#             post = Post.objects.get(id=id)
#             c_f = form.cleaned_data

#             comment = CommentPost.objects.create(
#                 comment_post=post,
#                 name=c_f.get("name"),
#                 comment_text=c_f.get("text"),
#                 comment_status=False
#             )
#             print(c_f)
#     post = Post.objects.get(id=id)
#     comment = post.comment.filter(comment_status=True)
#     form = Comment2()
#     print(comment)
#     print(post)
#     return render(
#         request=request,
#         template_name="blog/detail.html",
#         context={"post": post, "comment": comment, "form": form},
#     )
