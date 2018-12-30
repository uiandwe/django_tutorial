from django.shortcuts import render


def score(request):
    latest_question_list = ["데드풀1", "어벤져스", "슈퍼맨vs배트맨", "데드풀2"]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'score/score.html', context)