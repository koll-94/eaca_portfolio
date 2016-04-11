# -*- coding: utf-8 -*-
import functools
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from datetime import datetime
from main.models import FileExpansion
from main.models import DocType
from main.models import Document
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.views.generic.base import View
from django.http import *

def test(request):
    file_exp = FileExpansion.objects.filter()
    templ_data = {
        'file_exp': file_exp,
        'data': 'hello world',
        'date': "{:%Y %m %d}".format (datetime.now()),
        'time': "{:%H:%M}".format (datetime.now()),

    }
    return render_to_response('test.html', templ_data)


def private(request_number=0):
    """
        Декоратор, делат метод доступным только после авторизации.
        В противном случае отсылает на форму авторизации
        :param request_number - номер параметра запроса
    """
    def _wrap(method):
        @functools.wraps(method)
        def _wrapped(*args, **kwargs):
            try:
                request = args[request_number]
                if request.user.is_authenticated():
                    return method(*args, **kwargs)
                else:
                    return redirect('/')
            except:
                raise
        return _wrapped
    return _wrap


class EAuthenticationForm (AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super (EAuthenticationForm, self).__init__ (request, *args, **kwargs)
        self.fields['username'].label = u'Логин:'
        self.fields['password'].label = u'Пароль:'


class LoginFormView (FormView):
    form_class = EAuthenticationForm

    template_name = "login.html"
    success_url = "/main"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView (View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")


def main(reqwest):
    doc_type = DocType.objects.filter()
    templ_data = {
        'doctype': doc_type,
    }
    return render_to_response('main.html', templ_data)


@private()
def save_document (request, doc_type_id, name, year):
    obj_year = datetime.strptime(year, '%d.%m.%Y').date ()
    obj_doc_type_id = .objects.get (pk = course)
    obj_name = CourseState.objects.get (pk = state)
    obj_user = request.user
    UserCourseState.objects.update_or_create (user = obj_user, doc_type_id = obj_doc_type_id, year = obj_year, name = obj_name)
    return HttpResponseRedirect ("/grid_document/")


@private()
def grid_document(reqwest):
    document = Document.objects.filter()
    templ_data = {
        'doc': document,
    }
    return render_to_response('document_grid.html', templ_data)


@private()
def form_document(reqwest):
    pass