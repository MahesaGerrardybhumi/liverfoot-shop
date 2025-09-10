from django.shortcuts import render

def show_main(request):
    context = {
        'title': 'LiverFoot Shop',
        'name': 'Mahesa Gerrardybhumi',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
# Create your views here.
