from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from stats.models import Income, Outcome
from stats.serializers import IncomeSerializer, OutcomeSerializer


class IncomesAPIView(ListCreateAPIView):
    queryset = Income.objects.select_related('student', 'course')
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = IncomeSerializer


class IncomeAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Income.objects.select_related('student', 'course')
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = IncomeSerializer


class OutcomesAPIView(ListCreateAPIView):
    queryset = Outcome.objects.select_related('student', 'course')
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = OutcomeSerializer


class OutcomeAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Outcome.objects.select_related('student', 'course')
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = OutcomeSerializer