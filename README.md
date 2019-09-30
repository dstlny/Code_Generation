# PY Code Gen
Just something i wrote that allows you to prototype classes / functions within a JSON format.


Example of a JSON file below:

```JSON
{   
    "output_file_name": "this_file",
    "func_definitions": [
        {
            "decorators":[
                "@login_required",
                "@permission_required('this_is_a_permission')"
            ],
            "function_name": "this_is_a_function_with_decorators",
            "args": [
                "arg1",
                "arg2"
            ]
        },
        {
            "function_name": "this_is_a_function_without_decorators",
            "args": [
                "arg1",
                "arg2"
            ]
        }
    ],
    "class_definitions":[
        {   
            "decorators":[
                "@login_required",
                "@permission_required('this_is_a_permission')"
            ],
            "class_name":"this_is_a_test_class_with_decorators",
            "this_is_a_test_class_with_decorators_funcs": [
                {
                    "decorators":[
                        "@login_required",
                        "@permission_required('this_is_a_permission')"
                    ],
                    "function_name": "this_is_a_function_with_decorators",
                    "args": [
                        "arg1",
                        "arg2"
                    ]
                }
            ]
        },
        {   
            "class_name":"this_is_a_test_class_without_decorators",
            "this_is_a_test_class_without_decorators_funcs": [
                {
                    "function_name": "this_is_a_function_without_decorators",
                    "args": [
                        "arg1",
                        "arg2"
                    ]
                }
            ]
        },
        {  
            "decorators":[
                "@login_required",
                "@permission_required('this_is_a_permission')"
            ],  
            "class_name":"this_is_a_test_class_with_decorators",
            "this_is_a_test_class_with_decorators_funcs": [
                {
                    "function_name": "this_is_a_function_without_decorators",
                    "args": [
                        "arg1",
                        "arg2"
                    ]
                }
            ]
        },
        {  
            "decorators":[
                "@login_required",
                "@permission_required('this_is_a_permission')"
            ],  
            "class_name":"this_is_a_test_class_without_decorators",
            "this_is_a_test_class_without_decorators_funcs": [
                {   
                    "decorators":[
                        "@login_required",
                        "@permission_required('this_is_a_permission')"
                    ],
                    "function_name": "this_is_a_function_with_decorators",
                    "args": [
                        "arg1",
                        "arg2"
                    ]
                },
                {
                    "function_name": "this_is_a_function_without_decorators",
                    "args": [
                        "arg1",
                        "arg2",
                        "arg3",
                        "arg5"
                    ]
                }
            ]
        }
    ]
}

```

With these simple definitions, you can generate the following code:
```Python
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@login_required
@permission_required('this_is_a_permission')
def this_is_a_function_with_decorators(self, arg1, arg2):
	pass

def this_is_a_function_without_decorators(self, arg1, arg2):
	pass

## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@login_required
@permission_required('this_is_a_permission')
class this_is_a_test_class_with_decorators():

	@login_required
	@permission_required('this_is_a_permission')
	def this_is_a_function_with_decorators(self, arg1, arg2):
		pass

## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class this_is_a_test_class_without_decorators():

	def this_is_a_function_without_decorators(self, arg1, arg2):
		pass

## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@login_required
@permission_required('this_is_a_permission')
class this_is_a_test_class_with_decorators():

	def this_is_a_function_without_decorators(self, arg1, arg2):
		pass
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@login_required
@permission_required('this_is_a_permission')
class this_is_a_test_class_without_decorators():

	@login_required
	@permission_required('this_is_a_permission')
	def this_is_a_function_with_decorators(self, arg1, arg2):
		pass

	def this_is_a_function_without_decorators(self, arg1, arg2, arg3, arg5):
		pass

## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

Simply put: allows you to prototype class/view/function definitions.
