from django.shortcuts import render
# from django.http import HttpResponse


# Create your views here.
def index(request):
    context: dict[str, str] = {
        'caption': 'Lorem ipsum',
        'option' : 'active'
    }
    return render(request, 'main/lorem.html', context)


def info(request):
    context: dict[str, str] = {
        'caption': 'Что такое Lorem ipsum',
        'option': 'active'
    }
    return render(request, 'main/lorem_info.html', context)


def pan_eng(request):
    context: dict[str, str] = {
        'caption': 'Английские панграммы',
        'option': 'active'
    }
    return render(request, 'main/eng_pangrams.html', context)


def pan_rus(request):
    context: dict[str, str] = {
        'caption': 'Русские панграммы',
        'option': 'active'
    }
    return render(request, 'main/rus_pangrams.html', context)