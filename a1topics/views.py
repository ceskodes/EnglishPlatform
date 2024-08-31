from django.views.generic import TemplateView
from .models import A1Content
from englishcontent.models import EnglishContent

class MultiModelTemplateView(TemplateView):
    template_name = 'a1_topic_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['a1_content_list'] = A1Content.objects.all()
        context['english_content_list'] = EnglishContent.objects.all()
        return context