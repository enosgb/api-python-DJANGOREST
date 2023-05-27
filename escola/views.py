from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics,filters,views
from escola.models import Student, Course, Registration
from escola.serializer import StudentSerializer, CourseSerializer, RegistrationSerializer, ListRegistrationStudentsSerializer, ListaRegistrationsStudentsSerializer,ListCourseLevelsSerializer,ListRegistrationPeriodSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class StudentsViewSet(viewsets.ModelViewSet):
    '''Exibindo alunos e alunas'''
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class CoursesViewSet(viewsets.ModelViewSet):
    '''Exibindo todos os curso'''
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['description']
    
    
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class RegistrationsViewSet(viewsets.ModelViewSet):
    '''Listando todas as matriculas'''
    serializer_class = RegistrationSerializer
    def get_queryset(self):
        search = self.request.query_params.get('search',"")
        
        queryset = Registration.objects.filter(student__name__startswith=search)
        return queryset
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class ListRegistrationsStudent(generics.ListAPIView):
    '''Listando as matriculas de um aluno(a)'''

    def get_queryset(self):

        queryset = Registration.objects.filter(student_id=self.kwargs['pk'])
        print(queryset)
        return queryset
    serializer_class = ListRegistrationStudentsSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class ListStudentRegistrations(generics.ListAPIView):
    '''Listando alunos matriculados em um curso'''

    def get_queryset(self):
        queryset = Registration.objects.filter(course_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaRegistrationsStudentsSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]



class ListCourseLevels(views.APIView):
    
    def get(self,request):
        LEVEL = [
        {"value":'B',"option": 'Básico'},
        {"value":'I',"option": 'Intermediário'},
        {"value":'A',"option": 'Avançado'}]
        results = ListCourseLevelsSerializer(LEVEL, many=True).data
        return Response(results)
    
class ListRegistrationPeriod(views.APIView):
    def get(self,request):
        PERIOD = [
                {"value":'M',"option": 'Matutino'},
                {"value":'V',"option": 'Vespertino'},
                {"value":'N',"option": 'Noturno'}]
        results = ListRegistrationPeriodSerializer(PERIOD, many=True).data
        return Response(results)
    
    
