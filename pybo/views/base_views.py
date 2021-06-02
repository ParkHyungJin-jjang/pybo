from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question


def index(request):
    pageno=request.GET.get('page','1')
    question_list=Question.objects.order_by('-create_date')
    pages=Paginator(question_list, 10)
    onepage = pages.get_page(pageno)
    context = {'question_list': onepage}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)