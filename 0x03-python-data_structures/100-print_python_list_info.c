#include "Python.h"

/**
  * print_python_list_info - Prints information about python objects
  * @p: Pointer to the Python list object
  * Return: Nothing
  */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t i;
	Py_ssize_t list_size;
	Py_ssize_t allocated;
	PyObject *item;
	const char *item_type;
	PyListObject *list_object;

	list_object = (PyListObject *)p;
	list_size = PyList_Size(p);
	allocated = list_object->allocated;

	printf("[*] Size of the Python List: %zd\n", list_size);
	printf("[*] Allocated: %zd\n", allocated);

	for (i = 0; i < list_size; i++)
	{
		item = PyList_GetItem(p, i);
		item_type = Py_TYPE(item)->tp_name;
		printf("Element %zd: %s\n", i, item_type);
	}
}
