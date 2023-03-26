from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse

from ..models import Question
from ..views import QuestionList


def search(request) -> HttpResponse:
    """
    Search questions record for the given keywords
    """
    search_text = request.POST.get('search', False)
    if not search_text or request.method == 'GET':
        return redirect('/')
    search_keywords = search_text.split()
    my_filter_qs = Q()
    for search_keyword in search_keywords:
        my_filter_qs = my_filter_qs | Q(body__icontains=search_keyword) | \
            Q(title__icontains=search_keyword)
    question_list = Question.objects.filter(my_filter_qs)
    context = {'question_list': question_list}
    return render(request, "index.html", context)
