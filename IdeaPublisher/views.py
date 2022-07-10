# Create your views here.
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView
from fm.views import AjaxCreateView, AjaxUpdateView, AjaxDeleteView
from IdeaPublisher.models import Feedback, Idea
from IdeaPublisher.forms import FeedbackForm, MyRegistrationForm, UserEditForm, IdeaForm, IdeaUpdateForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView, TemplateView
from django.core.urlresolvers import resolve, reverse_lazy
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.core import serializers
from pure_pagination.mixins import PaginationMixin

def index(request):
    return HttpResponse("Hello Django!") 

def details(request):
    return render_to_response('feedback/details.html') 

class IndexView(TemplateView):
    template_name = 'IdeaPublisher/index.html'    

class AboutUsView(TemplateView):
    template_name = 'IdeaPublisher/AboutUs.html'

class ContactUsView(TemplateView):
    template_name = 'IdeaPublisher/ContactUs.html'    

#@login_required
class FeedbackListView(ListView):
    model = Feedback
    template_name = 'feedback/feedback_list.html'
    #paginate_by = 4

class IdeaListView(PaginationMixin, ListView):
    template_name = 'idea/idea_list.html'
    model = Idea
    paginate_by = 5
    def get_queryset(self):
        return Idea.objects.filter(estado='AV')

class IdeaDetailView(DetailView):
    template_name = 'idea/Details.html'
    model = Idea 	
    pk_url_kwarg = 'idea_pk'
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
         return super(IdeaDetailView, self).dispatch(*args, **kwargs)	
		
class MyIdeaListView(ListView):
    model = Idea
    template_name = 'idea/myidea_list.html'
    paginate_by = 5
    def get_queryset(self):
        self.owner = get_object_or_404(User, username=self.request.user)
        return Idea.objects.filter(owner_id=self.owner.id)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MyIdeaListView, self).dispatch(*args, **kwargs) 

#@login_required
class FeedbackCreateView(AjaxCreateView):
    form_class = FeedbackForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FeedbackCreateView, self).dispatch(*args, **kwargs)

from django.core.urlresolvers import reverse_lazy
class IdeaCreateView(AjaxCreateView):
    form_class = IdeaForm
    #success_url = reverse_lazy('ideas_list')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
         return super(IdeaCreateView, self).dispatch(*args, **kwargs)
    def get_form_kwargs(self):
        """This method is what injects forms with their keyword
            arguments."""
        # grab the current set of form #kwargs
        kwargs = super(IdeaCreateView, self).get_form_kwargs()
        # Update the kwargs with the user_id
        kwargs['user_as_owner'] = self.request.user
        return kwargs
    # def get_success_url(self):
        # return reverse_lazy('myideas_list')
    # def form_valid(self, form):
        # obj = form.save(commit=False)
        # obj.owner = self.request.user
        # obj.save()
        # return HttpResponseRedirect('../MyIdeas')    
    # def form_valid(self, form):
    #     candidate = form.save(commit=False)
    #     candidate.owner = self.request.user
    #     candidate.save()
    #     return HttpResponseRedirect(self.get_success_url())
    # def get_form_kwargs(self):
    #     kwargs = super(IdeaCreateView, self).get_form_kwargs()
    #     kwargs.update({'owner': self.request.user})
    #     return kwargs
    # def get_form_kwargs(self):
    #     kwargs = super(IdeaCreateView, self).get_form_kwargs()
    #     kwargs['owner'] = self.request.user

class IdeaUpdateView(AjaxUpdateView):
    message_template = "idea/idea_instance.html"
    form_class = IdeaUpdateForm
    model = Idea
    pk_url_kwarg = 'idea_pk'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IdeaUpdateView, self).dispatch(*args, **kwargs)            

#@login_required
class IdeaDeleteView(AjaxDeleteView):
    model = Idea
    pk_url_kwarg = 'idea_pk'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IdeaDeleteView, self).dispatch(*args, **kwargs)

#@login_required
class FeedbackUpdateView(AjaxUpdateView):

    message_template = "feedback/feedback_instance.html"
    form_class = FeedbackForm
    model = Feedback
    pk_url_kwarg = 'feedback_pk'

    def pre_save(self):
        self.object.update_count += 1

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FeedbackUpdateView, self).dispatch(*args, **kwargs)        

#@login_required
class FeedbackDeleteView(AjaxDeleteView):
    model = Feedback
    pk_url_kwarg = 'feedback_pk'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FeedbackDeleteView, self).dispatch(*args, **kwargs)

def nuevo_usuario(request):
    if request.method == 'POST':
        formulario = MyRegistrationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = MyRegistrationForm()
    return render_to_response('registration/newUser.html',{'formulario':formulario}, context_instance = RequestContext(request))

class UserEdit(UpdateView):
    model = User
    form_class = UserEditForm
    success_url = reverse_lazy('settings_change_done')
    template_name = 'accounts/settings.html'
 
    def get_object(self, queryset=None):
        return self.request.user
		
from django.http import JsonResponse

from django.db.models import Q

def get_ideas(request):
    if request.is_ajax():
        #q = request.GET.get('term', '')
        q = request.POST['search']
        drugs = Idea.objects.filter((Q(titulo__startswith = q) | Q(titulo__icontains = q)) & Q(estado='AV'))
        #drugs = Idea.objects.filter(titulo = q )
        results = []
        for drug in drugs:
            drug_json = {}
            drug_json['id'] = drug.pk
            drug_json['label'] = drug.titulo
            drug_json['value'] = drug.titulo
            results.append(drug_json)
        #data = simplejson.dumps(results)
        # return JsonResponse([{'id': o.id, 'label': o.titulo}
            # for o in drugs], safe=False)
        data = serializers.serialize('json', drugs)
        return HttpResponse(data,'json')
    else:
        return JsonResponse({'error': 'Not Ajax or no GET'})    
        #data = serializers.serialize('json', results)
    # else:
        # data = 'fail'
    # mimetype = 'application/json'
    # return HttpResponse(data, mimetype)   
	
	
def get_myideas(request):
    if request.is_ajax():
        q = request.POST['search']
        drugs = Idea.objects.filter((Q(titulo__startswith = q) | Q(titulo__icontains = q)) & Q(estado='AV') & Q(owner=request.user.id))
        results = []
        for drug in drugs:
            drug_json = {}
            drug_json['id'] = drug.pk
            drug_json['label'] = drug.titulo
            drug_json['value'] = drug.titulo
            results.append(drug_json)
        data = serializers.serialize('json', drugs)
        return HttpResponse(data,'json')
    else:
        return JsonResponse({'error': 'Not Ajax or no GET'})