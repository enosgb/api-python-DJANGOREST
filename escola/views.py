from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class AlunosViewSet(viewsets.ModelViewSet):
    '''Exibindo alunos e alunas'''
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class CursosViewSet(viewsets.ModelViewSet):
    '''Exibindo todos os curso'''
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class MatriculasViewSet(viewsets.ModelViewSet):
    '''Listando todas as matriculas'''
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
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


class ListRegistrations(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.all()
        return queryset
    serializer_class = MatriculaSerializer
