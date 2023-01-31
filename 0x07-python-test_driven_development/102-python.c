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
	char *s;
	Py_ssize_t len;
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
			len = PyBytes_Size(enc);
			s = PyBytes_AsString(enc);
			printf("  length: %zd\n", len);
			printf("  value: %s\n", s);
			Py_DECREF(enc);
		}
	}
	else if (PyBytes_Check(p))
	{
		printf("[.] string object info\n");
		printf("  type: compact ascii\n");

		len = PyBytes_Size(p);
		s = PyBytes_AsString(p);
		printf("  length: %zd\n", len);
		printf("  value: %s\n", s);
	}
	else
	{
		printf("[ERROR] Invalid String Object\n");
	}
}
