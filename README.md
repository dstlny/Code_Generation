# PY Code Gen
Just something i wrote that allows you to prototype classes / functions within a JSON format.


Example of a JSON file below:

```JSON
{   
    "output_file_name": "this_file", // this is the file that you waqnt to output to
    "func_definitions": [ // arrray of function definitions that are outside of a class
        {
            "decorators":[
                "@login_required",
                "@permission_required('this_is_a_permission')"
            ],  // optional
            "function_name": "this_is_a_function_with_decorators",
            "args": [
                "arg1",
                "arg2"
            ]  // optional
        }
    ],
    "class_definitions":[ // array of class definitions
        {  
            "decorators":[
                "@login_required",
                "@permission_required('this_is_a_permission')"
            ],  // decorators for the class
            "class_name":"this_is_a_test_class_without_decorators", // name of the class
            "this_is_a_test_class_without_decorators_funcs": [ // this name must coincide with the classes name + _funcs
                {   
                    "decorators":[
                        "@login_required",
                        "@permission_required('this_is_a_permission')"
                    ], // optional
                    "function_name": "this_is_a_function_with_decorators",
                    "args": [
                        "arg1",
                        "arg2"
                    ] // optional
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
