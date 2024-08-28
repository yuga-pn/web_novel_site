from django.shortcuts import render
from django.views.generic import ListView ,DeleteView
from web_novel.models import Novel
# Create your views here.

class NovelList(ListView):
    model=Novel
    context_object_name="novels"
    template_name="web_novel/novel_list.html"
    
    def get_queryset(self):
        query=self.request.GET.get("query")
        if query:
            nov_list=Novel.objects.filter(work_name__icontains=query) | Novel.objects.filter(tag__icontains=query)| Novel.objects.filter(title__icontains=query)
            
        else:
            nov_list=Novel.objects.all()
        return nov_list
    
        
    
class NovelDetail(DeleteView):
    model=Novel
    context_object_name="novel"
    template_name="web_novel/novel_detail.html"
    
class TitleList(ListView):
    model=Novel
    context_object_name="titles"
    template_name="web_novel/title_list.html"