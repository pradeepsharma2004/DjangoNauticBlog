from django.shortcuts import render


def articles_list(request):
    return render(request, 'articles_list.html')
