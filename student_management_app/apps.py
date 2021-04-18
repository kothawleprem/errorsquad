from django.apps import AppConfig


class StudentManagementAppConfig(AppConfig):
    name = 'student_management_app'

'''# apps.py

from django.apps import AppConfig

def do_stuff(sender, **kwargs):
    mymodel = sender.get_model('models')
    mymodel.objects.get() # etc...

class StudentManagementAppConfig(AppConfig):
    name = 'student_management_app'

    def ready(self):
        post_migrate.connect(do_stuff, sender=self)'''