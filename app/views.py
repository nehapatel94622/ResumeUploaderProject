from django.shortcuts import render
from .form import ResumeForm
from .models import ResumeModel
from django.views import View

# Create your views here.
class HomeView(View):
    def get(self, request):
        form = ResumeForm()
        candidates = ResumeModel.objects.all()
        return render(request, 'index.html', {'candidates':candidates ,'form':form})

    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'index.html', {'form':form})


class CandidateView(View):
    def get(self, request, pk):
        candidate = ResumeModel.objects.get(pk=pk)
        print(pk)
        return render(request, 'candidate1.html', {'candidate':candidate})
