#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: PyObject pointer
 * Return: Nothing
 */

void print_python_list_info(PyObject *p)
{
	int size = PyList_Size(p), i = 0;
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;
	PyObject *element;

	if (!PyList_Check(p))
	{
		printf("Input is not a Python list\n"), return;
	}
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %ld\n", allocated);
	for (i = 0; i < size; i++)
	{
		element = PyList_GetItem(p, i);
		printf("Element %d: ", i);
		if (PyLong_Check(element))
		{
			printf("int");
		}
		else if (PyFloat_Check(element))
		{
			printf("float");
		}
		else if (PyTuple_Check(element))
		{
			printf("tuple");
		}
		else if (PyList_Check(element))
		{
			printf("list");
		}
		else if (PyStr_Check(element))
		{
			printf("str");
		}
		else
		{
			PyObject_Print(element, stdout, 0);
		}
		printf("\n");
	}
}
