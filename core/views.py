from django.shortcuts import render,HttpResponseRedirect

# Create your views here.
from .forms import QuestionForm, AnswerForm
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Question, Answer, Liked

def home(request):
    quest_list = Question.objects.all()[:15]
    context = {'quest_list':quest_list}
    return render(request, 'home.html', context)

from django.shortcuts import render, get_object_or_404, redirect

def create_question(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = QuestionForm(request.POST)
            if form.is_valid():
                question = form.save(commit=False)
                question.author = request.user
                question.save()
                return HttpResponseRedirect(reverse('question_detail', args=[question.pk]))
        else:
            form = QuestionForm()

        return render(request, 'create_question.html', {'form': form})
    else:
        return HttpResponseRedirect(reverse('account:login'))



# def question_detail(request, pk):
#     question = get_object_or_404(Question, pk=pk)
#     answers = question.answer_set.all()
   

#     if request.method == 'POST':
#         form = AnswerForm(request.POST)
#         if form.is_valid():
#             my_answer = form.save(commit=False)
           
#             my_answer.question = question
#             my_answer.author = request.user
           
#             my_answer.save()
#             return redirect('question_detail', pk=question.pk)
#     else:
#         form = AnswerForm()
#         context = {
#         'question': question,
#         'answers': answers,
#         'form': form, }
#     return render(request, 'question_detail.html', context)


def like_answer(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    liked, created = Liked.objects.get_or_create(answer=answer, user=request.user)
    if not created:
        liked.delete()
    return HttpResponseRedirect(reverse('question_detail', args=[answer.question.pk]))

def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = question.answer_set.all()
    liked_answers = request.user.answer_likes.values_list('answer', flat=True)

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            my_answer = form.save(commit=False)
           
            my_answer.question = question
            my_answer.author = request.user
           
            my_answer.save()
            return redirect('question_detail', pk=question.pk)
    else:
        form = AnswerForm()
        context = {
        'question': question,
        'answers': answers,
        'liked_answers': liked_answers,
        'form': form, }
    return render(request, 'question_detail.html', context)