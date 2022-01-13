from django.db.models import query
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
#from .models import model_name


def home(request):
    return render(request, 'view/home.html')


# def search(request):
#    query_list = model_name.objects.order_by('emp_id')
#    if 'search' in request.GET:
#        search = request.GET['search']
#        if search:
#            query_list = query_list.filter(emp_id__iexact=search)
#    context = {
#        'list' : query_list,
#    }
#
#    return render(request, 'views/search.html',context)