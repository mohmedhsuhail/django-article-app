from django.contrib.auth.models import User 
from django.db.models.signals import post_save
from django.dispatch import receiver
from . import tasks

@receiver(post_save,sender=User)
def send_registration_mail(sender,instance,created,**kwargs):
	if created:
		print(instance.email)
		tasks.send_mail_task(instance.username,instance.email)
		#tasks.send_mail_task.delay(instance.username,instance.email)  #run this instead for sending mail using Celery server