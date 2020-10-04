from django.views.generic import ListView
from django.shortcuts import render
from . models import Letter, JoinLetter


# class HomeView(ListView):
#     context_object_name = 'name'
#     template_name = 'home.html'
#     # queryset = JoinLetter.objects.all()
    

#     def get_context_data(self, **kwargs):
#         context = super(HomeView, self).get_context_data(**kwargs)
#         context['joinLetter'] = self.JoinLetter.objects.all()
#         context['letters'] = Letter.objects.get(letter=kwargs['letter'])
#         return context

def letter_detail_view(request, inletter):
    result = Letter.objects.filter(letter=inletter)
    join_letter_result = JoinLetter.objects.all().order_by('id')
    context = {'letter': inletter, 'results': result, 'join_letters': join_letter_result}
    return render(request, 'home.html', context)






    

   