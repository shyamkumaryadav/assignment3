from rest_framework.serializers import HyperlinkedModelSerializer
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import FilterSet, OrderingFilter
from .models import Student

def Handler404(request, exception):
    return render(request, template_name="404.html", context={exception: exception})


class StudentSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'url', 'name', 'rollNo', 'physics', 'chemistry', 'maths', 'total', 'percentage']
        extra_kwargs = {
            'url': {'lookup_field': 'rollNo'},
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
            'name': ['icontains'],
            'rollNo': ['exact'],
        }

class StudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_field = 'rollNo'
    filterset_class = MyFilterSet