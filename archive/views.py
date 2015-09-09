from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

from .models import Featured, Series

def index(request):
    featured = Featured.objects.order_by('featured__pub_date')
    all_series = Series.objects.order_by('name')
    context = { 'featured': featured, 'all_series': all_series }
    return render(request, 'archive/index.html', context)

def series(request, seriesName):
    series = Series.objects.get(name=seriesName)
    sermons = series.sermon_set.order_by('pub_date', 'sequence_num')
    context = { 'sermons': sermons, 'series': series}
    return render(request, 'archive/series.html', context)
