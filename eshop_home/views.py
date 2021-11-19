from django.shortcuts import render


# Create your views here.
def home_page(request):
    context = {}
    return render(request, 'home_page/home_page.html', context)


def header_page(request):
    context = {}
    return render(request, 'shared/header.html', context)


def footer_page(request):
    context = {}
    return render(request, 'shared/footer.html', context)



