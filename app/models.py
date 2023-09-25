from django.db import models


class Audit(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.CharField(max_length=20)
    camera_id = models.CharField(max_length=30)
    lens_id = models.CharField(max_length=30)
    SD_card = models.CharField(max_length=30)
    datetime_out = models.DateTimeField("Date device out")
    datetime_in = models.DateTimeField("Date device in", default=None, blank=True, null=True)
    condition = models.CharField(max_length=500, default=None, blank=True, null=True)
