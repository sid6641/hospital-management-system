from django.db import models
status_choice=(('0','Waiting'),('1','Pending'),('2','Completed'))
# Create your models here.
class Request(models.Model):
	name = models.CharField(max_length = 140)
	reg_no = models.CharField(max_length = 10, unique=True)
	problem= models.CharField(max_length = 140)
	submit_date = models.DateTimeField()
	appoint_date = models.DateTimeField()
	appoint_no = models.IntegerField(unique = True)
	doctor = models.ForeignKey('Doctor')
	done = models.BooleanField(default = False)
	outsider = models.BooleanField(default= False)
	status =  models.CharField(max_length=1 ,choices=status_choice)
	
	def __unicode__(self):
		return self.name

