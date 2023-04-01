from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response

from django.db.models import Q, Count
from django.utils import timezone
from drf_yasg.utils import swagger_auto_schema

from stats.models import Income, Outcome
from edu.models import Student, Teacher, Course, FormRequest
from stats.serializers import IncomeSerializer, OutcomeSerializer, FilterSerializer
from stats.queries import get_stats


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


class StatsAPIView(APIView):

    @swagger_auto_schema(query_serializer=FilterSerializer)
    def get(self, request):
        year = request.query_params.get('year', timezone.now().year)
        data = get_stats({'year': year})
        data.update({
            'request_forms': FormRequest.objects.aggregate(
                requested=Count('is_seen', Q(is_seen=False), distinct=True),
                approved=Count('is_seen', Q(is_seen=True), distinct=True),
            ),
            'students': Student.objects.count(),
            'teachers': Teacher.objects.count(),
            'courses': Course.objects.aggregate(
                inactive=Count('status', Q(status=False), distinct=True),
                active=Count('status', Q(status=True), distinct=True),
            ),
            })

        return Response(data)
