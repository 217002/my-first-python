from django.shortcuts import render

# Create your views here.
def index(request):
    """학습 로그 홈페이지"""
    return render(request, 'learning_logs/index.html')
