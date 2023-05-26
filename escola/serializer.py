from calendar import c
from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from escola.models import Aluno,Curso,Matricula

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id','nome','rg','cpf','data_nascimento']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'
    def to_representation(self, instance):    
        rep = super(CursoSerializer, self).to_representation(instance)        
        rep['nivel'] = instance.get_nivel_display()  
        return rep

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = "__all__"
    def to_representation(self, instance):    
        rep = super(MatriculaSerializer, self).to_representation(instance)        
        rep['curso'] = instance.curso.descricao
        rep['aluno'] = instance.aluno.nome    
        rep["periodo"] = instance.get_periodo_display()  
        return rep

class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
    def get_periodo(self,obj):
        return obj.get_periodo_display()

class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
        model = Matricula
        fields = ['aluno_nome']