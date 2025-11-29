from django.shortcuts import render

def home(request):
    return render(request, 'up.html')

def bn(request):
    return render(request, 'varanasi.html')

def kashi(request):
    return render(request, 'kashivishwanath.html')

def ghat(request):
    return render(request, 'dhasashwamedhghat.html')

def aarti(request):
    return render(request, 'gangaaarti.html')