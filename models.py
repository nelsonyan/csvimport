

from django.db import models
from django.urls import reverse
from employee.models import EmployeeList
from django.contrib.admin.widgets import AdminDateWidget

class Category(models.Model):
    category = models.CharField(max_length = 50, unique = True)
    def __str__(self):
        return self.category

class Status(models.Model):
    status = models.CharField(max_length = 50, unique = True)
    def __str__(self):
        return self.status

class TrackHeader(models.Model):
    report_key = models.AutoField(primary_key=True)
        #show pk in display but not editable
    category = models.ForeignKey(Category, on_delete = models.SET_NULL, null = True, blank = True)
    task_name = models.CharField(max_length = 80, blank = True)
    dead_line = models.CharField(null = True, blank = True, max_length = 50)
    requested_by = models.ForeignKey(EmployeeList, on_delete = models.SET_NULL, null = True, blank = True, related_name = 'requested_by')
        #related_name made doulbe Foreign key possible, why?
    date_requested = models.CharField(null = True, blank = True, max_length = 50)
    assigned_to = models.ForeignKey(EmployeeList, on_delete = models.SET_NULL, null = True, blank = True)
    status = models.ForeignKey(Status, on_delete = models.SET_NULL, null = True, blank = True)
    sku_count = models.CharField(max_length = 100, blank = True)
    sell_sheet = models.BooleanField(default = True)
    pog_render = models.BooleanField(default = True)
    artwork_design = models.BooleanField(default = True)
    mockup = models.BooleanField(default = True)
    comments = models.TextField(max_length = 5000, blank = True)

    # class Meta:
        # ordering = ["-report_key"]
            #this puts the latest highest PK on top of report list. for CBV
            #this replace 'report_output = TrackHeader.objects.order_by('-report_key')' in view.py if doing CBV
    def get_absolute_url(self):
        return reverse('report:track_report')
            #cannot add kwargs here, or update will not come back to track_report

    def __int__(self):
        return self.pk
        #don;t know how to show this properly
