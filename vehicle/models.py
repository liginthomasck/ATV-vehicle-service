from django.db import models

class vitem(models.Model):
	vehid = models.IntegerField()
	mno = models.CharField(max_length=50)
	mname = models.CharField(max_length=50)
	color = models.CharField(max_length=50)
	scap = models.CharField(max_length=50)
	fea = models.CharField(max_length=50)
	mil = models.CharField(max_length=50)
	amt = models.CharField(max_length=50)
	status = models.CharField(max_length=50)
	img = models.FileField(upload_to='viedos')
	class Meta:
		db_table = "vehicle"