from __future__ import absolute_import
from celery import shared_task
from capp.models import Code

@shared_task
def run_script(sub_id):	
	s=Code.objects.get(pk=sub_id[0])
	s.sub_result="<div class='alert alert-success'> small one done! end-start:seconds! </div>"
	s.save()
