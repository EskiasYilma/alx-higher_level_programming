#include "Python.h"
/**
  * print_python_list_info - Prints information about python objects
  * @p: PyObject pointer to print info about
  * Return: Nothing
  */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, size, allocated;
	PyObject *item;
	const char *item_type;
	PyListObject *list_object;

	list_object = (PyListObject *)p;
	size = PyList_Size(p);
	allocated = list_object->allocated;

	printf("[*] Size of the Python List = %d\n", (int) size);
	printf("[*] Allocated = %d\n", (int)allocated);
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		item_type = Py_TYPE(item)->ob_size->tp_name;
		printf("Element %d: %s\n", (int) i, item_type);
	}
}
