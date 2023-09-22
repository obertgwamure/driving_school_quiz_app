import os
from django.db import models
from django.conf import settings
from quizes.models import Quiz


# generating unique file names for image uploads
def question_image_path(instance, filename):
    filename = os.path.basename(filename)  # remove any directory paths from filename
    return os.path.join(settings.BASE_DIR, f'static/images/quiz-assets/questions/{instance.id or 1}/{filename}')

def answer_image_path(instance, filename):
    filename = os.path.basename(filename)  # remove any directory paths from filename
    return os.path.join(settings.BASE_DIR, f'static/images/quiz-assets/questions/{instance.question.id}/{instance.id}/{filename}')


# Create your models here.


class Question(models.Model):
    text = models.CharField(max_length=540)
    image = models.ImageField(upload_to=question_image_path, blank=True, max_length=1000)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created = models.DateField(auto_now=True)
    
    def __str__(self):
        return str(self.text)
    
    def get_answers(self):
        return self.answer_set.all()



class Answer(models.Model):
    text = models.CharField(max_length=240)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=answer_image_path, blank=True, max_length=1000)
    created = models.DateField(auto_now=True)
    
    def __str__(self):
        return f'question {self.question.text}, answer: {self.text}: correct: {self.correct}'
    




