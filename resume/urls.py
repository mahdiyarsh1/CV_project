from django.urls import path
from .views import index, download_resume, show_bamdad, show_cs50x, show_cando, blog
from django.views.generic import TemplateView
app_name = "resume"
urlpatterns = [
    path("", index, name="index"),
    path("home/", index, name="index"),
    # path("post/<int:id>", post_details, name="post_d"),
    path('download/resume/', download_resume, name='download_resume'),
    path('bamdad/', show_bamdad, name='bamdad'),
    path('cs50x/', show_cs50x, name='cs50'),
    path('cando/', show_cando, name='cando'),
    path('blog_1', blog, name="blog_1")
    # path('contact/', contact_view, name='contact_view'),
    # path('success/', success_view, name='success'),
]

# مسیر ناشناخته به 404 منتقل می‌شود
# path("<path:resource>", index, name="index")
