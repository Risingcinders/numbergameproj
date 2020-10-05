from django.shortcuts import render, HttpResponse, redirect
import random


def index(request):
    toolow = False
    toohigh = False
    justright = False
    lose = False
    if request.method == 'POST':
        guess = int(request.POST['guess'])
    else:
        guess = 0
    if 'target' in request.session:
        if guess < request.session['target']:
            toolow = True
        elif guess > request.session['target']:
            toohigh = True
        else:
            justright = True
        request.session['counter'] += 1
    else:
        request.session['target'] = random.randrange(1, 100)
        request.session['counter'] = 0

    if request.session['counter'] >= 5:
        lose = True
    context = {
        'target': request.session['target'],
        'guess': guess,
        'low': toolow,
        'high': toohigh,
        'correct': justright,
        'count': request.session['counter'],
        'loser': lose
    }
    return render(request, "index.html", context)


def kill(request):
    del request.session['target']
    return redirect('/')
