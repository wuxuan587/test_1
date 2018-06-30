
from django.shortcuts import render
from goal.models import team,record
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.http import HttpResponse
from goal.models import CJsonEncoder

import json
import requests

# Create your views here.

def worldcup_team(requests):
    res=team.objects.all()
    current_page=requests.GET.get('pages')
    per_page=requests.GET.get('per_page')
    room_list=[]
    for room in res:
        room_info = dict()
        room_info['group_id'] =room.group_id
        room_info['team_name'] = room.team_name
        room_info['team_point'] = room.team_point
        room_info['team_goal'] = room.team_goal
        room_info['team_fumble'] = room.team_fumble
        room_info['team_point'] = room.team_point
        room_info['team_goaldifference'] = room.team_goaldifference
        room_info['team_won'] = room.team_won
        room_info['team_draw'] = room.team_draw
        room_info['team_lose'] = room.team_lose
        room_list.append(room_info)

    paginator =Paginator(room_list, per_page)  # show 8 contacts per page
    customer=paginator.page(current_page)
    msg = 'get team msg successfully!'
#    ret_body = dict(code=0, masg=msg, data=customer)
    folders = json.dumps(customer.object_list,ensure_ascii=False) #added .object_list
    return HttpResponse(folders)

 #   return HttpResponse(json.dumps(ret_body,ensure_ascii=False))

def worldcup_goal(requests):
    res=team.objects.all().order_by("group_id","-team_goaldifference")
    room_list = []
    i=5
    for room in res:
        room_info = dict()
        room_info['group_id'] = room.group_id
        room_info['team_name'] = room.team_name
        room_info['team_point'] = room.team_point
        room_info['team_goal'] = room.team_goal
        room_info['team_fumble'] = room.team_fumble
        room_info['team_point'] = room.team_point
        room_info['team_goaldifference'] = room.team_goaldifference
        room_info['team_won'] = room.team_won
        room_info['team_draw'] = room.team_draw
        room_info['team_lose'] = room.team_lose
        i-=1
        if(i==4):
            room_list.append(room_info)
        elif(i==1):
            i=5


    msg = 'get team msg successfully!'
    ret_body = dict(code=0, masg=msg, data=room_list)
    return HttpResponse(json.dumps(ret_body, ensure_ascii=False))

def worldcup_gap(requests):
    res=record.objects.order_by("-team_goaldifference","-match_date")
    room_list = []
    i=0
    for room in res:
        room_info = dict()
        room_info['match_date'] = room.match_date
        room_info['team_against'] = room.team_against
        i+=1
        if(i<4):
            room_list.append(room_info)

    msg = 'get team msg successfully!'
    ret_body = dict(code=0, masg=msg, data=room_list)
    return HttpResponse(json.dumps(ret_body, cls=CJsonEncoder ,ensure_ascii=False))


def wordcup_promotion(requests):
    res=team.objects.order_by("group_id","-team_point","team_goaldifference","team_name")
    room_list = []
    i=5
    for room in res:
        room_info = dict()
        room_info['group_id'] = room.group_id
        room_info['team_name'] = room.team_name
        room_info['team_point'] = room.team_point
        room_info['team_goal'] = room.team_goal
        room_info['team_fumble'] = room.team_fumble
        room_info['team_point'] = room.team_point
        room_info['team_goaldifference'] = room.team_goaldifference
        room_info['team_won'] = room.team_won
        room_info['team_draw'] = room.team_draw
        room_info['team_lose'] = room.team_lose
        i-=1
        if(i>2):
            room_list.append(room_info)
        elif(i==1):
            i=5

    msg = 'get team msg successfully!'
    ret_body = dict(code=0, masg=msg, data=room_list)
    return HttpResponse(json.dumps(ret_body, cls=CJsonEncoder ,ensure_ascii=False))