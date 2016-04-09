from django.shortcuts import render_to_response
from datetime import datetime
from main.models import FileExpansion

def test(request):
    file_exp = FileExpansion.objects.filter()
    templ_data = {
        'file_exp': file_exp,
        'data': 'hello world',
        'date': "{:%Y %m %d}".format (datetime.now()),
        'time': "{:%H:%M}".format (datetime.now()),

    }
    return render_to_response ('test.html', templ_data)

