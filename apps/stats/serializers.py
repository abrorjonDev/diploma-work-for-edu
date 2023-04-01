from rest_framework import serializers
from django.forms import model_to_dict
from stats.models import Income, Outcome


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.course:
            data['course'] = model_to_dict(instance.course, fields=('id', 'title', 'status'))
        if instance.student:
            data['student'] = model_to_dict(instance.student, fields=('fish', 'id', 'contact', 'level'))
        return data


class OutcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outcome
        fields = "__all__"


class FilterSerializer(serializers.Serializer):
    year = serializers.IntegerField(required=False)