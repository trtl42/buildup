from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Person, Pots
import math


def index(request):

    #
    member_list = Person.objects.order_by('id')

    context = {'member_list': member_list}

    return render(request, 'gst/member_list.html', context)

def pots(request):

    # 포트 리스트
    pot_list = Person.objects.order_by('id')

    # 배정 대상 인원
    member_list = Person.objects.filter(team=5)

    # 팀 배정 인원
    team_member = Person.objects.exclude(team=5)

    # 포트
    pot_list = list(pot_list)
    pot1 = list()
    pot2 = list()
    pot3 = list()
    pot4 = list()
    pot5 = list()
    pot6 = list()

    for i in pot_list:
        if (i.pot == 1):
            pot1.append(i)
        if (i.pot == 2):
            pot2.append(i)
        if (i.pot == 3):
            pot3.append(i)
        if (i.pot == 4):
            pot4.append(i)
        if (i.pot == 5):
            pot5.append(i)
        if (i.pot == 6):
            pot6.append(i)

    print(pot_list)
    print(pot1)

    # print(member_list1.values())
    # <variable name>[index]['key']

    # 배정 대상 인원 리스트 2열
    member_list = list(member_list)

    # for i in member_list:
    # print(i.name)

    # 인원수 리스트 생성 시 1,2열 인원 수 나누기
    cnt = len(member_list)
    cnt1 = math.ceil(cnt / 2)
    cnt2 = math.ceil(cnt1 + 1)

    if (cnt1 == 1):
        cnt2 = 1

    # print(cnt1)
    # print(cnt2)

    # 1,2열 인원 나열
    member_list1 = member_list[:int(cnt1)]
    member_list2 = member_list[int(cnt2):]

    # 팀 인원
    team_member = list(team_member)
    team1 = list()
    team2 = list()
    team3 = list()
    team4 = list()

    for i in team_member:
        if (i.team == 1):
            team1.append(i)
        if (i.team == 2):
            team2.append(i)
        if (i.team == 3):
            team3.append(i)
        if (i.team == 4):
            team4.append(i)

    #print(team1)

    context = {'member_list1': member_list1, 'member_list2': member_list2,
               'team1': team1, 'team2': team2,
               'team3': team3, 'team4': team4,
               'pot1': pot1, 'pot2':pot2,
               'pot3': pot3, 'pot4':pot4,
               'pot5': pot5, 'pot6':pot6,}

    return render(request, 'gst/member_pots.html', context)