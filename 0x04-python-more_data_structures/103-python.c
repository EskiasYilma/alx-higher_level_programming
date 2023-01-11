#include "Python.h"
#include <stdio.h>
#include <string.h>


/**
  * print_python_bytes - Prints information about python byte objects
  * @p: PyObject pointer to print info about
  * Return: Nothing
  */
void print_python_bytes(PyObject *p)
{
	char *data;
	int i, len;


	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	data = ((PyBytesObject *)p)->ob_sval;
	len = ((PyVarObject *)p)->ob_size;

	printf("  size: %d\n", (int)len);
	printf("  trying string: %s\n", data);
	if (len < 10)
		printf("  first %d bytes:", len + 1);
	else
		printf("  first 10 bytes:");

	for (i = 0; i < (len < 10 ? len : 10); i++)
	{
		printf(" %.2x", (unsigned char)data[i]);
	}
	printf("\n");
}


/**
  * print_python_list - Prints information about python list objects
  * @p: PyObject pointer to print info about
  * Return: Nothing
  */
void print_python_list(PyObject *p)
{
	Py_ssize_t i, size, allocated;
	PyObject *item;
	const char *item_type;
	PyListObject *list_object;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	list_object = (PyListObject *)p;
	size = (((PyVarObject *)(p))->ob_size);
	allocated = list_object->allocated;

	printf("[*] Size of the Python List = %d\n", (int) size);
	printf("[*] Allocated = %d\n", (int)allocated);
	for (i = 0; i < size; i++)
	{
		item = ((PyListObject *)p)->ob_item[i];
		item_type = (((PyObject *)(item))->ob_type)->tp_name;
		printf("Element %d: %s\n", (int) i, item_type);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}

