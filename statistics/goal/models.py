from django.db import models
import json
import datetime
import time

# Create your models here.

class team(models.Model):
    team_id=models.AutoField(primary_key=True)
    team_name=models.CharField(max_length=5)
    group_id=models.CharField(max_length=2,blank=True)
    team_point=models.CharField(max_length=2,blank=True)
    team_goal=models.CharField(max_length=2,blank=True)
    team_fumble=models.CharField(max_length=2,blank=True)
    team_goaldifference=models.CharField(max_length=2,blank=True)
    team_won=models.CharField(max_length=2,blank=True)
    team_draw=models.CharField(max_length=2,blank=True)
    team_lose=models.CharField(max_length=2,blank=True)

class record(models.Model):
    match_id=models.AutoField(primary_key=True)
    group_id=models.CharField(max_length=2,blank=True)
    team_against=models.CharField(max_length=20,blank=True)
    match_date=models.DateField(blank=True,null=True)
    home_team_score=models.CharField(max_length=2,null=True)
    visit_team_score=models.CharField(max_length=2,null=True)
    team_goaldifference=models.CharField(max_length=2,null=True)


class CJsonEncoder(json.JSONEncoder):
        def default(self,obj):
                if isinstance(obj,datetime.datetime):
                        return obj.strftime('%Y-%m-%d %H:%M:%S')
                elif isinstance(obj,datetime.date):
                        return obj.strftime("%y-%m-%d")
                elif isinstance(obj,time.time()):
                        return obj.strftime("%H:%M:%S")
                else:
                        return json.JSONEncoder.default(self.obj)