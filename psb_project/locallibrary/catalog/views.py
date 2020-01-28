from django.shortcuts import render
from django.http import Http404, HttpResponse, JsonResponse
from django.template import loader
from catalog.models import *
from django.forms.models import model_to_dict
import random
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
import json
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
    #print(context)
    #
    # get related questions and pass to html template
    module_id = list(modules.objects.filter(module_name=context['module']['module_name']).values("id"))[0]['id']
    question = list(questions.objects.all().filter(questions_under_id=module_id))
    random.shuffle(question)
    context['question'] = question
    #print(context)
    #
    #get related answers and pass to html template
    #print(question)
    for i in question:
        questions_id.append(i.id)
    #print(questions_id)
    for id in questions_id:
        related_choices.append(list(answers.objects.filter(answers_under_id=id)))
    context['answer'] = related_choices
    #print(context['answer'])
    #
    # get Id & scores and pass to html template
    Scores = scores.objects.order_by('scores').reverse()
    context['scores'] = Scores
    return HttpResponse(template.render(context,request))

def newScore(request):
    print("SUCCESS : AJAX ENTERED!")
    template = loader.get_template('template.html')
    context = {}
    #object1 = request.POST['gameId']
    #object2 = request.POST['scores']
    #print(object1)
    #print(object2)
    #new_object = scores(gameId=object1, scores=object2).save()
    if request.method == "POST" :
        # handle save logic
        if request.body:
            jsonLoad = json.loads(request.body)
            Scores = jsonLoad['scores']
            username = jsonLoad['username']
        else :
            return JsonResponse({"errors": ["POST object has insufficient parameters!"]})
        errors = scores(scores=Scores, gameId=username)
        errors.save()
    return HttpResponse(template.render(context,request))
    