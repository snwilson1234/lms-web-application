from django.shortcuts import render

# Create your views here.

def sample_class_view(request):
    print(request.headers)
    return render(request, "sampleclass/sample_class.html", {})