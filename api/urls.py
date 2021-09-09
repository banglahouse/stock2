from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('stocks/', views.getStocks),
    path('stocks/<str:pk>', views.getStock),
    path('articles/', views.getArticles),
    path('articles/<str:pk>', views.getArticle),
    path('options/', views.getOptions),
    path('options/<str:pk>', views.getOption),
    path('investment/', views.getInvestments),
    path('investment/<str:pk>', views.getInvestment),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
