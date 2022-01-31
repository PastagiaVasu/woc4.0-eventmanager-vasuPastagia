from django.db import models

class event_tbl(models.Model):
    class Meta:
        verbose_name_plural = "Events"

    name = models.CharField(max_length=50)
    description = models.TextField()
    poster_link = models.TextField()
    start_date = models.DateTimeField(blank=True,null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    deadLine = models.DateField(blank=True, null=True)
    host_email = models.EmailField()
    host_password = models.TextField()

    def __str__(self):
        return self.name

class participant_tbl(models.Model):
    name = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    event_name = models.CharField(max_length=50)
    registration_type = models.CharField(max_length=10)
    no_of_people = models.CharField(max_length=100, default="1")

    def __str__(self):
        return self.name
