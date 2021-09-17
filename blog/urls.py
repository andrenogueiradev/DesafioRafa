from blog.models import Category
from django.conf.urls import include
from django.urls import path
from . import views
from . views import HomeView, ArticleDetailView, CategoryView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('ckeditor/', include ('ckeditor_uploader.urls')),
    path('category/<str:cats>/', CategoryView, name='category')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
