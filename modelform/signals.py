
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.mail import send_mail 
from .models import mark, stu

 
 
@receiver(post_save, sender=stu)
def create_mark(sender, instance, created, **kwargs):
    if created:
        print("signal cretaed")
        mark.objects.create(student=instance)
  
@receiver(post_save, sender=mark)
def save_mark(sender, instance, **kwargs):
        print("signals saved")
        instance.student.save()
        print(instance.student)
       
        send_mail('mail', 'your mark is now {} '.format(instance.mark), "Don't Reply <do_not_reply@domain.example>", ['{}'.format(instance.student)])
