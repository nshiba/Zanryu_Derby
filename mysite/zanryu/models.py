from django.db import models

class Person(models.Model):
    student_id = models.CharField(max_length=7)
    name = models.TextField()
    now_entry_exit = models.BooleanField()

    def __unicode__(self):
        return self.student_id

class Log(models.Model):
    student_id = models.CharField(max_length=7)
    entry_exit = models.BooleanField()
    dump_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.student_id

class MyStatus(models.Model):
    student_id = models.ForeignKey(to_field=Person.student_id)
    zanryu_kaisu = models.IntegerField()
