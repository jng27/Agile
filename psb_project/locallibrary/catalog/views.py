from django.shortcuts import render
from django.http import Http404, HttpResponse, JsonResponse
from django.template import loader
from catalog.models import *
from django.forms.models import model_to_dict
import random
# Create your views here.

def index(request):
    template = loader.get_template('template.html')
    context = {}
    questions_id = []
    related_choices = []
    # get all available modules and randomly pick one
    module = list(modules.objects.all().values('module_name'))
    randomed = [i for i in range(len(module))]
    random.shuffle(randomed)
    context['module'] = module[randomed[0]]
    print(context)
    #
    # get related questions and pass to html template
    module_id = list(modules.objects.filter(module_name=context['module']['module_name']).values("id"))[0]['id']
    question = list(questions.objects.all().filter(questions_under_id=module_id))
    context['question'] = question
    print(context)
    #
    #get related answers and pass to html template
    print(question)
    for i in question:
        questions_id.append(i.id)
    print(questions_id)
    for id in questions_id:
        related_choices.append(list(answers.objects.filter(answers_under_id=id)))
    context['answer'] = related_choices
    print(context['answer'])
    return HttpResponse(template.render(context,request))