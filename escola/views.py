from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics,filters,views
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosSerializer,ListCourseLevelsSerializer,ListRegistrationPeriodSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class AlunosViewSet(viewsets.ModelViewSet):
    '''Exibindo alunos e alunas'''
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome']
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class CursosViewSet(viewsets.ModelViewSet):
    '''Exibindo todos os curso'''
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['descricao']
    
    
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class MatriculasViewSet(viewsets.ModelViewSet):
    '''Listando todas as matriculas'''
    serializer_class = MatriculaSerializer
    def get_queryset(self):
        search = self.request.query_params.get('search',"")
        
        queryset = Matricula.objects.filter(aluno__nome__startswith=search)
        return queryset
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class ListaMatriculasAluno(generics.ListAPIView):
    '''Listando as matriculas de um aluno(a)'''

    def get_queryset(self):

        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        print(queryset)
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class ListaAlunosMatriculados(generics.ListAPIView):
    '''Listando alunos matriculados em um curso'''

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]



class ListCourseLevels(views.APIView):
    
    def get(self,request):
        NIVEL = [
        {"value":'B',"option": 'BÁSICO'},
        {"value":'I',"option": 'Intermediário'},
        {"value":'A',"option": 'Avançado'}]
        results = ListCourseLevelsSerializer(NIVEL, many=True).data
        return Response(results)
    
class ListRegistrationPeriod(views.APIView):
    def get(self,request):
        PERIODO = [
                {"value":'M',"option": 'Matutino'},
                {"value":'V',"option": 'Vespertino'},
                {"value":'N',"option": 'Noturno'}]
        results = ListRegistrationPeriodSerializer(PERIODO, many=True).data
        return Response(results)
    
    
