from celery import shared_task
from django.core.mail import send_mail

from time import sleep 



@shared_task
def send_mail_task(user_name,user_email):
	#sleep(7)
	send_mail('BloggerWheel',
			  'Hey {},Thanks for signing up to BloggerWheel!'.format(user_name),
			  'mohmedhsuhail@gmail.com',
			  [user_email,])
	return None