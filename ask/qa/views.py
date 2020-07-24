from django.http import HttpResponse 
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from qa.models import Question, Answer
from django.core.paginator import Paginator, EmptyPage

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def get_render(questions, html):
    try:
        limit = int(request.GET.get('limit', 10))
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(questions, limit)
    paginator.baseurl = '?page='
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, html, 
        {
            'questions': page.object_list,
            'paginator': paginator,
            'page': page,
        }
    )

@require_GET
def questions_new(request):
    return get_render(Question.objects.new(),
                      'qa/questions_new.html')

@require_GET
def questions_popular(request):
    return get_render(Question.objects.popular(),
                      'qa/questions_popular.html')

@require_GET
def question_info(request, q_id):
    question = get_object_or_404(Question, id=q_id)
    try:
        answers = question.answer_set.all()[:]
    except Answer.DoesNotExist:
        answers = None
    return render(request, 'qa/question_info.html',
        {
            'question': question,
            'answers': answers,
        }
    )
