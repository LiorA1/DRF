
from rest_framework import serializers
from .models import Language, Paradigm, Programmer

# Like using ModelForm when working with forms

class LanguageSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Language
		fields = ['id', 'url', 'name', 'paradigm']

#? I really need to use 'HyperlinkedModelSerializer' ?
#? It seems that 'ModelSerializer' function in the same manner.
class ParadigmSerializer(serializers.ModelSerializer):

	class Meta:
		model = Paradigm
		fields = ['id', 'url', 'name']


class ProgrammerSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Programmer
		fields = ['id', 'url', 'name', 'languages']