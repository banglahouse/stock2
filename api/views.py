
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import serializers
from .models import stock, articles,optionsStocks,investments
from .serializers import articleApiSerializers, stockApiSerializers,optionsApiSerializers,investmentsApiSerializers
from django.utils.html import escape

@api_view(['GET'])
def getInvestments (request):
    investment = investments.objects.all().order_by('-timeStamp')
    serializer = investmentsApiSerializers(investment, many= True)
    return Response(serializer.data)

@api_view(['GET'])
def getInvestment (request, pk):
    investmentSingle = investments.objects.get(id=pk)
    serializer = investmentsApiSerializers(investmentSingle, many= False)
    return Response(serializer.data)




@api_view(['GET'])
def getOptions (request):
    options = optionsStocks.objects.all().order_by('-timeStamp')
    serializer = optionsApiSerializers(options, many= True)
    return Response(serializer.data)

@api_view(['GET'])
def getOption (request, pk):
    optionsSingle = optionsStocks.objects.get(id=pk)
    serializer = stockApiSerializers(optionsSingle, many= False)
    return Response(serializer.data)
    
@api_view(['GET'])
def getStocks (request):
    stocks = stock.objects.all().order_by('-timeStamp')
    serializer = stockApiSerializers(stocks, many= True)
    return Response(serializer.data)

@api_view(['GET'])
def getStock (request, pk):
    stockSingle = stock.objects.get(id=pk)
    serializer = stockApiSerializers(stockSingle, many= False)
    return Response(serializer.data)
    

@api_view(['GET'])

def getArticles (request):

    articlesNew = articles.objects.all().order_by('-created_at')
    serializer = articleApiSerializers(articlesNew, many= True)
    # return Response(escape(serializer.data))
    return Response(serializer.data)
    # return HttpResponse(escape(serializer.data))


@api_view(['GET'])
def getArticle (request, pk):
    articlesSingle = articles.objects.get(id=pk)
    serializer = articleApiSerializers(articlesSingle, many= False)
    return Response(serializer.data)
    # return Response(escape(serializer.data))
