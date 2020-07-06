from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Question

# Create your views here


# Index view
def index(request):
    return render(request, 'polls/index.html')


# View list function based-view
def view_list(request):

    """  """

    list_questions = Question.objects.all()
    context = {'questions': list_questions}
    return render(request, 'polls/list.html', context)


# view detail - function based-view
def view_detail(request, poll_id):

    """ View Detail Question and Vote - Function"""

    question = get_object_or_404(Question, pk=poll_id)
    return render(request, 'polls/detail.html', {'question': question})


# result view - function based-view
def view_result(request, poll_id):

    """  """

    question = get_object_or_404(Question, pk=poll_id)
    return render(request, 'polls/result.html', {'question': question})


# vote view - function based-view
def view_vote(request, poll_id):

    """  """

    question = get_object_or_404(Question, pk=poll_id)
    try:
        data = request.POST['answer']
        selected_choice = question.choice_set.get(pk=data)
    except:
        return render(request, 'polls/detail.html',
                      {
                          'question': question,
                          'error_message': "ERROR with answer of this question."
                      })
    selected_choice.vote += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:result', args=(question.id, )))
