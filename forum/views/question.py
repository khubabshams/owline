from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from ..models import Question
from ..forms import AnswerForm


class QuestionList(generic.ListView):
    model: Question
    queryset = Question.objects.filter(archive=False).order_by('-created_on')
    template_name = 'index.html'
    paginated_by = 5


class QuestionDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Question.objects.filter(archive=False)
        question = get_object_or_404(queryset, slug=slug)
        answers = question.answers.filter(archive=False).order_by('-votes')
        context = {
            'question': question,
            'answers': answers,
            'answer_form': AnswerForm()
        }
        return render(request, "question.html", context)

    def post(self, request, slug, *args, **kwargs):
        queryset = Question.objects.filter(archive=False)
        question = get_object_or_404(queryset, slug=slug)
        answers = question.answers.filter(archive=False).order_by('votes')

        answer_form = AnswerForm(data=request.POST)
        answer = answer_form.save(commit=False)
        answer.created_by = request.user
        answer.modified_by = request.user
        answer.related_question = question

        if answer_form.is_valid():
            answer_form.instance.email = request.user.email
            answer_form.instance.name = request.user.username
            answer.save()
        else:
            answer_form = AnswerForm()

        context = {
            'question': question,
            'answers': answers,
            'answer_form': AnswerForm()
        }
        return render(request, "question.html", context)
