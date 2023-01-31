#include <Python.h>
#include <ctype.h>
#include <stddef.h>

/**
 * print_python_string - prints Python strings
 * @p: string pointer
 * Return: Nothing
 */

void print_python_string(PyObject *p)
{
	char *str;
	Py_ssize_t size;
	PyObject *enc, *bytes;

	if (PyUnicode_Check(p))
	{
		printf("[.] string object info\n");
		printf("  type: compact ");
		if (PyUnicode_IS_COMPACT_ASCII(p))
			printf("ascii\n");
		else
			printf("unicode object\n");

		enc = PyUnicode_AsEncodedString(p, "utf-8", "strict");
		if (enc == NULL)
			PyErr_Clear();
		else
		{
			size = PyBytes_Size(enc);
			str = PyBytes_AsString(enc);
			printf("  length: %zd\n", size);
			printf("  value: %s\n", str);
			Py_DECREF(enc);
		}
	}
	else if (PyBytes_Check(p))
	{
		printf("[.] string object info\n");
		printf("  type: compact ascii\n");

		size = PyBytes_Size(p);
		str = PyBytes_AsString(p);
		printf("  length: %zd\n", size);
		printf("  value: %s\n", str);
	}
	else
	{
		printf("[ERROR] Invalid String Object\n");
	}
}
