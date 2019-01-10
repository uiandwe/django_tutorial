
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template.context_processors import csrf
from django.contrib import auth
from django.shortcuts import redirect


from user_manager.forms import LoginForm



def login(request):

    template = get_template('login_form.html')
    context = {'login_form' : LoginForm()}
    context.update(csrf(request))
    return HttpResponse(template.render(context))


def login_validate(request):
    login_form_data = LoginForm(request.POST)
    if login_form_data.is_valid():
        user = auth.authenticate(username=login_form_data.cleaned_data['id'], password=login_form_data.cleaned_data['password'])

        if user is not None:
            if user.is_active:
                auth.login(request, user)
                request.session.set_expiry(86400)
                return redirect('/board/')

        else:
            return HttpResponse('사용자가 없거나 비밀번호가 틀림')

    else:
        return HttpResponse('로그인 폼 비정상')

    return HttpResponse('그냥 오류')
