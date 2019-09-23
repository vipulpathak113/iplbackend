from rest_framework import serializers

from .models import PointsTable


class TeamlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointsTable
        fields = ('id', 'team_name', 'played', 'won', 'lost', 'no_result', 'points', 'nrr')
