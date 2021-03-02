from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import FilterSet, OrderingFilter
from .models import Student

class StudentSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'url', 'name', 'rollNo', 'physics', 'chemistry', 'maths', 'total', 'percentage']
        extra_kwargs = {
            'url': {'lookup_field': 'name'},
        }
        
class MyFilterSet(FilterSet):
    o = OrderingFilter(
        fields=(
            ('rollNo', 'rollNo'),
            ('physics', 'physics'),
            ('chemistry', 'chemistry'),
            ('maths', 'maths'),
            ('total', 'total'),
            ('percentage', 'percentage'),
        ),
        
    )
    class Meta:
        model = Student
        fields = {
            'name': ['contains'],
            'rollNo': ['exact'],
        }

class StudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    lookup_field = 'name'
    filterset_class = MyFilterSet

    def get_queryset(self):
        try:
            return Student.objects.all()
        except:
            return None
    