from django.shortcuts import render

def index(request):
    latest_question_list = ["test", "test1"]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'movies/index.html', context)

