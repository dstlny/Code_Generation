import json

## lets read the file in first
def read_json(path):
	
	with open(path) as json_file:
		data = json.load(json_file)

	if 'output_file_name' in data:
		this_file = data['output_file_name']+'.py'
	else:
		this_file = None

	do_something_with_json(data, this_file)


def do_something_with_json(data, output_file=None):

	function_to_add = []
	decorators = False

	with open(output_file, 'a+') as python_file:
		python_file.write('## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
		python_file.write('\r\n')

	if 'func_definitions' in data:

		for json_entry in data['func_definitions']:

			if output_file:
				
				with open(output_file, 'a+') as python_file:

					if 'decorators' in json_entry:

						for decorator in json_entry['decorators']:
							function_to_add.append(decorator.strip()+'\n')
					
					function_to_add.append('def {0}(self, '.format(json_entry['function_name'].replace(' ', '_').replace('-', '_')))
		
					if json_entry['args']:
						for i, args in enumerate(json_entry['args']):
							if i < len(json_entry['args'])-1:
								function_to_add.append("{0}, ".format(args.strip()))	
							else:
								function_to_add.append("{0}".format(args.strip()))
						else:
							function_to_add.append('):')
						
					else:
						function_to_add.append('self):')
					
					line = ''.join([x for x in function_to_add])
					python_file.write(line.strip())
					python_file.write('\n\tpass\n\n')
					function_to_add = []
					line = ""
		else:
			with open(output_file, 'a+') as python_file:
				python_file.write('## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
				python_file.write('\r\n')

	classes_to_add = []
	line = ""
	class_decorators = False

	if 'class_definitions' in data:

		for i, class_entry in enumerate(data['class_definitions']):

			if output_file:

				with open(output_file, 'a+') as python_file:

					if 'decorators' in class_entry:

						for decorator in class_entry['decorators']:
							classes_to_add.append(decorator.strip()+'\n')
							class_decorators = True
						
						classes_to_add.append('class {0}():'.format(class_entry['class_name'].replace(' ', '_').replace('-', '_').strip()))
						classes_to_add.append('\n')
						classes_to_add.append('\n')
					else:
						classes_to_add.append('\n\nclass {0}():'.format(class_entry['class_name'].replace(' ', '_').replace('-', '_').strip()))
						classes_to_add.append('\n')
						classes_to_add.append('\n')
					
					class_name = class_entry['class_name'].replace(' ', '_').replace('-', '_')
			
					func_names = class_name+'_funcs'

					for functions in class_entry[func_names]:
						if 'decorators' in functions:

							for decorator in functions['decorators']:
								classes_to_add.append('\t'+decorator.strip()+'\n')

						if 'args' in functions:

							classes_to_add.append('\tdef {0}(self, '.format(functions['function_name'].replace(' ', '_').replace('-', '_').strip()))

							for i, args in enumerate(functions['args']):
								if i < len(functions['args'])-1:
									classes_to_add.append("{0}, ".format(args.strip()))	
								else:
									classes_to_add.append("{0}".format(args.strip()))
							else:
								classes_to_add.append('):')
						else:
							classes_to_add.append('\tdef {0}(self):'.format(functions['function_name'].replace(' ', '_').replace('-', '_').strip()))
						
						line = ''.join([x for x in classes_to_add])
						python_file.write(line.strip())
						python_file.write('\n\t\tpass')
						python_file.write('\n\n')
						python_file.write('\t')
						classes_to_add = []
						line = ""

					else:
						python_file.write('\r\n')
						python_file.write('## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

			with open(output_file, 'a+') as python_file:
				python_file.write('\r\n')
		
	
read_json('Untitled-1.json')