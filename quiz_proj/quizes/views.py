''''from django.shortcuts import render
from .models import Quiz
from django.views.generic import ListView
from django.http import JsonResponse
# Create your views here.

class QuizListView(ListView):
    model = Quiz
    template_name = 'quizes/main.html'
    
def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    
    return render(request, 'quizes/quiz.html', {'obj':quiz})

def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })
        
'''      
        


from django.conf import settings
from django.shortcuts import render
from .models import Quiz
from django.views.generic import ListView
from django.http import JsonResponse
from django.urls import reverse

# Create your views here.

class QuizListView(ListView):
    model = Quiz
    template_name = 'quizes/main.html'

def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)

    return render(request, 'quizes/quiz.html', {'obj':quiz})

def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answer_data = {'answer_text': a.text}
            if a.image:
                answer_data['image'] = a.image.url
            answers.append(answer_data)
        question_data = {'question_text': q.text, 'answers': answers}
        if q.image:
            question_data['image'] = q.image.url
        questions.append(question_data)
    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })
