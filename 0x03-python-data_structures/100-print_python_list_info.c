#include "Python.h"

/**
  * print_python_list_info - Prints information about python objects
  * @p: Pointer to the Python list object
  * Return: Nothing
  */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, list_size, temp_alloc;
	PyObject *item;
	const char *item_type;
	PyListObject *list_object;

	list_object = (PyListObject *)p;
	list_size = PyList_Size(p);
	temp_alloc = list_object->allocated;

	printf("[*] Size of the Python List: %d\n", (int) list_size);
	printf("[*] Allocated: %d\n", (int) temp_alloc);

	for (i = 0; i < list_size; i++)
	{
		item = PyList_GetItem(p, i);
		item_type = Py_TYPE(item)->tp_name;
		printf("Element %d: %s\n", (int) i, item_type);
	}
}
