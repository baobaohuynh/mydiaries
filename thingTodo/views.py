from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Topic 
from .forms import TopicForm
from django.http import Http404


# Create your views here.
def index(request):
    return render(request, "thingTodo/index.html")


@login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by("-date_added")        
    context = {'topics': topics}

    return render(request, "thingTodo/topics.html", context)


@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user: 
        raise Http404
    context = {'topic': topic}
    return render(request, "thingTodo/topic.html", context)


@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect("thingTodo:topics")

    context = {'form': form}
    return render(request, "thingTodo/new_topic.html", context)


@login_required
def edit_topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user: 
        raise Http404
    if request.method != 'POST':
        form = TopicForm(instance=topic)
    else: 
        form = TopicForm(instance=topic, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("thingTodo:topics")
    
    context = {'topic': topic, 'form': form}
    return render(request, "thingTodo/edit_topic.html", context)
