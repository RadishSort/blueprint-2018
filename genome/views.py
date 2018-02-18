from django.shortcuts import render

from .models import Trait
import genomelink

def index(request):
	# gets list of traits
	traits_list_object = Trait.objects.all()

	traits_list = [t.trait_name for t in traits_list_object]

	context = {
		'traits_list': traits_list,
	}

	return render(request, 'genome/index.html', context)
'''
	# join traits into list
	traits_list = ', '.join([t.trait_name for t in traits_list])

	outputs_list = []

	for trait in traits_list:
		outputs_list.append( genomelink.Report.fetch(name=output, population='european', token='GENOMELINKTEST001').summary['text'] )

	trait_dict = {}

	context = {
		'traits_list': traits_list,
		'traits_output': traits_output,
	}
'''