from django.shortcuts import render

# Create your views here.
def conditional(request):
    d={'a':10}
    return render(request,'conditional.html',d)


def conditional(request):
    d={'a':20,'b':30}
    return render(request,'conditional.html',d)


def conditional(request):
    d={'a':876,'b':789,'c':786}
    return render(request,'conditional.html',d)


def conditional(request):
    d={'u':234,'s':678,'g':543}
    return render(request,'conditional.html',d)





