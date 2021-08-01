from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('stocks/', views.getStocks),
     path('stocks/<str:pk>', views.getStock),
     path('articles/', views.getArticles),
       path('articles/<str:pk>', views.getArticles),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)