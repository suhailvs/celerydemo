from django.shortcuts import render
from django.http import HttpResponse
from capp.models import Code
from capp.tasks import run_script
# Create your views here.
def home(request):
	return render(request,'home.html')

def get_log(request):	
	sub_id=request.session.get('sub_id', False)
	if not sub_id:  return HttpResponse('nocontent')
	s=Code.objects.get(id=sub_id)
	results = s.sub_result
	if results:
		del request.session['sub_id']
	
	return HttpResponse(results)
    
def addcode(request):  
	c=Code(codes=request.GET['codes'])
	c.save()

	# Run the code and check for errors.
	res=run_script.delay((c.pk,))

	request.session['sub_id']=c.pk	
	return HttpResponse('Please wait, we will show the code status soon.')