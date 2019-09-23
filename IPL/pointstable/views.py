from .serializers import TeamlistSerializer
from .models import PointsTable
from rest_framework import generics
from django.shortcuts import render
from django.template.context import RequestContext
import requests


def home(request):
    response = requests.get('https://push.sportskeeda.com/cricket-points-table/ipl')
    teamdata = response.json()
    from operator import itemgetter
    teamdata = sorted(teamdata, key=itemgetter('points'), reverse=True)
    for i in teamdata:
        p = PointsTable.objects.filter(team_name=i['team_name']).update(played=i['played'], won=i['won'],
                                                                        lost=i['lost'], no_result=i['no_result'],
                                                                        points=i['points'], nrr=i['nrr'])
    from pycricbuzz import Cricbuzz
    c = Cricbuzz()
    matches = c.matches()
    for i in matches:
        for k, v in i.items():
            if i['srs'] == "Indian Premier League 2019":
                mid=i['id']
                break
    lscore = c.livescore("22460")
    return render(request, 'pointstable/home.html', context={'matches': matches,'teamdata':teamdata,'lscore':lscore})

class CreateView(generics.ListCreateAPIView):
    queryset = PointsTable.objects.all().order_by('-points', '-nrr')
    serializer_class = TeamlistSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PointsTable.objects.all()
    serializer_class = TeamlistSerializer

    def perform_create(self, serializer):
        serializer.save()
