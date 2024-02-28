#include <stdio.h>
#include <Python.h>
#include <unistd.h>
#include <sys/mman.h>
#include <arpa/inet.h>
#include "ipdb.h"

typedef struct {
    PyObject_HEAD
    char *path;
    ipdb_reader *reader;
    PyObject **fields;
    /* Type-specific fields go here. */
} PyIPDB_Object;


// Module method definitions
static PyObject* ipdb_find(PyIPDB_Object *ps, PyObject *args) {
    int len;
    PyObject *ipobj;
    const char *ip;
    u_char *l_ip;
    const char *lang;
    unsigned char ip_bits = 0;
    PyObject* ret_dict;
    char body[512];
    int node = 0;
    int err;
    struct in_addr addr4;
    struct in6_addr addr6;
    
    if (!PyArg_ParseTuple(args, "O|s", &ipobj, &lang)) {
        return NULL;
    }
    // ipobj
    // TypeError
    PyObject* pyStr;
    if (PyLong_Check(ipobj))
    {
        addr4.s_addr = htonl(PyLong_AsLong(ipobj));
        l_ip = &addr4.s_addr;
        ip_bits = 32;
    } else if (PyUnicode_Check(ipobj))
    {
        pyStr = PyUnicode_AsEncodedString(ipobj, "utf-8", "Error ~");
    } else if (PyBytes_Check(ipobj))
    {
        if (PyBytes_Size(ipobj) == 4)
        {
            l_ip = PyBytes_AS_STRING(ipobj);
            ip_bits = 32;
        } else if (PyBytes_Size(ipobj) == 16)
        {
            l_ip = PyBytes_AS_STRING(ipobj);
            ip_bits = 128;
        } else 
        {
            pyStr = ipobj;
        }
    } else {
        PyErr_SetString(PyExc_TypeError,
                        "Invalid Type of IP");
        return NULL;
    }
    if (!ip_bits)
    {
        ip = PyBytes_AS_STRING(pyStr);
        Py_XDECREF(pyStr);

        if (inet_pton(AF_INET, ip, &addr4)) {
            ip_bits = 32;
            l_ip = &addr4.s_addr;
        } else if (inet_pton(AF_INET6, ip, &addr6)) {
            ip_bits = 128;
            l_ip = &addr6.s6_addr;
        } else {
            PyErr_SetString(PyExc_TypeError,
                            "Invalid IP Format");
            Py_XDECREF(ip);
            Py_RETURN_NONE;
        }
        Py_XDECREF(ip);
    }

    int off = -1;
    if (lang == NULL)
    {
        off = 0;
    } else
    {
        for (int i = 0; i < ps->reader->meta->language_length; ++i) {
            if (strcmp(lang, ps->reader->meta->language[i].name) == 0) {
                off = ps->reader->meta->language[i].offset;
                break;
            }
        }
        if (off == -1) {
            PyErr_SetString(PyExc_TypeError,
                            "Error, Unsupport Language");
            Py_RETURN_NONE;
        }
    }

    // ipv4
    if (ip_bits == 32 && !ipdb_reader_is_ipv4_support(ps->reader)) {
        PyErr_SetString(PyExc_TypeError,
                        "Error, the database is not support IPv4");
        Py_RETURN_NONE;
    }
    if (ip_bits == 128 && !ipdb_reader_is_ipv6_support(ps->reader)) {
        PyErr_SetString(PyExc_TypeError,
                        "Error, the database is not support IPv6");
        Py_RETURN_NONE;
    }

    err = ipdb_search(ps->reader, (const u_char *) l_ip, ip_bits, &node);

    if (err != ErrNoErr) {
        Py_RETURN_NONE;
    }
    const char *content;

    err = ipdb_resolve(ps->reader, node, &content);
    if (err != ErrNoErr) {
        Py_RETURN_NONE;
    }
    size_t p = 0, o = 0, s = 0, e = 0;
    len = ps->reader->meta->fields_length;

    ret_dict = PyList_New(ps->reader->meta->fields_length);;
    int p1 = 0, p2 = -1;

    while (*(content + p)) {
        if (*(content + p) == '\t') {
            if (o >= len)
            {
                PyErr_SetString(PyExc_TypeError,
                                "Error, the database is damaged");
                Py_RETURN_NONE;
            }
            PyObject *d_value = PyUnicode_FromStringAndSize(content + p2 + 1, p - 1 - p2);
            PyList_SetItem(ret_dict, o, d_value);
            p2 = p;
            ++o;
        }
        if ((!e) && o == off + len) {
            e = p;
        }
        ++p;
        if (off && (!s) && o == off) {
            s = p;
        }
    }
    if (!e) e = p;
    PyObject *d_value = PyUnicode_FromStringAndSize(content + p2 + 1, p - 1 - p2);
    PyList_SetItem(ret_dict, o, d_value);
    if (off + len > o + 1) {
        PyErr_SetString(PyExc_TypeError,
                        "Error, the database is damaged");
        Py_RETURN_NONE;
    }
    return ret_dict;
}


// Module method definitions
static PyObject* ipdb_find_map(PyIPDB_Object *ps, PyObject *args) {
    int len;
    PyObject *ipobj;
    const char *ip;
    u_char *l_ip;
    const char *lang;
    unsigned char ip_bits = 0;
    PyObject* ret_dict;
    char body[512];
    int node = 0;
    int err;
    struct in_addr addr4;
    struct in6_addr addr6;
    
    if (!PyArg_ParseTuple(args, "O|s", &ipobj, &lang)) {
        return NULL;
    }
    // ipobj
    // TypeError
    PyObject* pyStr;
    if (PyLong_Check(ipobj))
    {
        addr4.s_addr = htonl(PyLong_AsLong(ipobj));
        l_ip = &addr4.s_addr;
        ip_bits = 32;
    } else if (PyUnicode_Check(ipobj))
    {
        pyStr = PyUnicode_AsEncodedString(ipobj, "utf-8", "Error ~");
    } else if (PyBytes_Check(ipobj))
    {
        if (PyBytes_Size(ipobj) == 4)
        {
            l_ip = PyBytes_AS_STRING(ipobj);
            ip_bits = 32;
        } else if (PyBytes_Size(ipobj) == 16)
        {
            l_ip = PyBytes_AS_STRING(ipobj);
            ip_bits = 128;
        } else 
        {
            pyStr = ipobj;
        }
    } else {
        PyErr_SetString(PyExc_TypeError,
                        "Invalid Type of IP");
        return NULL;
    }
    if (!ip_bits)
    {
        ip = PyBytes_AS_STRING(pyStr);
        Py_XDECREF(pyStr);

        if (inet_pton(AF_INET, ip, &addr4)) {
            ip_bits = 32;
            l_ip = &addr4.s_addr;
        } else if (inet_pton(AF_INET6, ip, &addr6)) {
            ip_bits = 128;
            l_ip = &addr6.s6_addr;
        } else {
            PyErr_SetString(PyExc_TypeError,
                            "Invalid IP Format");
            Py_XDECREF(ip);
            Py_RETURN_NONE;
        }
        Py_XDECREF(ip);
    }

    int off = -1;
    if (lang == NULL)
    {
        off = 0;
    } else
    {
        for (int i = 0; i < ps->reader->meta->language_length; ++i) {
            if (strcmp(lang, ps->reader->meta->language[i].name) == 0) {
                off = ps->reader->meta->language[i].offset;
                break;
            }
        }
        if (off == -1) {
            PyErr_SetString(PyExc_TypeError,
                            "Error, Unsupport Language");
            Py_RETURN_NONE;
        }
    }

    // ipv4
    if (ip_bits == 32 && !ipdb_reader_is_ipv4_support(ps->reader)) {
        PyErr_SetString(PyExc_TypeError,
                        "Error, the database is not support IPv4");
        Py_RETURN_NONE;
    }
    if (ip_bits == 128 && !ipdb_reader_is_ipv6_support(ps->reader)) {
        PyErr_SetString(PyExc_TypeError,
                        "Error, the database is not support IPv6");
        Py_RETURN_NONE;
    }

    err = ipdb_search(ps->reader, (const u_char *) l_ip, ip_bits, &node);

    if (err != ErrNoErr) {
        Py_RETURN_NONE;
    }
    const char *content;

    err = ipdb_resolve(ps->reader, node, &content);
    if (err != ErrNoErr) {
        Py_RETURN_NONE;
    }
    size_t p = 0, o = 0, s = 0, e = 0;
    len = ps->reader->meta->fields_length;

    ret_dict = PyDict_New();
    int p1 = 0, p2 = -1;

    while (*(content + p)) {
        if (*(content + p) == '\t') {
            if (o >= len)
            {
                PyErr_SetString(PyExc_TypeError,
                                "Error, the database is damaged");
                Py_RETURN_NONE;
            }
            PyObject *d_value = PyUnicode_FromStringAndSize(content + p2 + 1, p - 1 - p2);
            PyDict_SetItem(ret_dict, ps->fields[o], d_value);
            Py_XDECREF(d_value);
            p2 = p;
            ++o;
        }
        if ((!e) && o == off + len) {
            e = p;
        }
        ++p;
        if (off && (!s) && o == off) {
            s = p;
        }
    }
    if (!e) e = p;
    PyObject *d_value = PyUnicode_FromStringAndSize(content + p2 + 1, p - 1 - p2);
    PyDict_SetItem(ret_dict, ps->fields[o], d_value);
    Py_XDECREF(d_value);
    if (off + len > o + 1) {
        PyErr_SetString(PyExc_TypeError,
                        "Error, the database is damaged");
        Py_RETURN_NONE;
    }
    return ret_dict;
}


// Module method definitions
static PyObject* ipdb_languages(PyIPDB_Object *ps, PyObject *args) {
    PyObject *ret_dict = PyList_New(ps->reader->meta->language_length);
    for (int i = 0; i < ps->reader->meta->language_length; ++i) {
        PyObject *d_value = PyUnicode_FromString(ps->reader->meta->language[i].name);
        PyList_SetItem(ret_dict, i, d_value);
    }
    return ret_dict;
}


// Module method definitions
static PyObject* ipdb_fields(PyIPDB_Object *ps, PyObject *args) {
    PyObject *ret_dict = PyList_New(ps->reader->meta->fields_length);
    for (int i = 0; i < ps->reader->meta->fields_length; ++i) {
        Py_XINCREF(ps->fields[i]);
        PyList_SetItem(ret_dict, i, ps->fields[i]);
    }
    return ret_dict;
}


// Module method definitions
static PyObject* ipdb_is_support_ipv4(PyIPDB_Object *ps, PyObject *args) {
    if (ipdb_reader_is_ipv4_support(ps->reader)){
        Py_RETURN_TRUE;
    } else {
        Py_RETURN_FALSE;
    }
}


// Module method definitions
static PyObject* ipdb_is_support_ipv6(PyIPDB_Object *ps, PyObject *args) {
    if (ipdb_reader_is_ipv6_support(ps->reader)){
        Py_RETURN_TRUE;
    } else {
        Py_RETURN_FALSE;
    }
}


// Module method definitions
static PyObject* ipdb_build_time(PyIPDB_Object *ps, PyObject *args) {
    return PyLong_FromLongLong(ps->reader->meta->build_time);
}


// Method definition object for this extension, these argumens mean:
// ml_name: The name of the method
// ml_meth: Function pointer to the method implementation
// ml_flags: Flags indicating special features of this method, such as
//          accepting arguments, accepting keyword arguments, being a
//          class method, or being a static method of a class.
// ml_doc:  Contents of this method's docstring
static PyMethodDef ipdb_methods[] = {
    {   
        "find", ipdb_find, METH_VARARGS,
        "Search for IP."
    },
    {   
        "find_map", ipdb_find_map, METH_VARARGS,
        "Search for IP."
    },
    {
        "languages", ipdb_languages, METH_NOARGS,
        "Get support languages."
    },
    {
        "fields", ipdb_fields, METH_NOARGS,
        "Get support fields."
    },
    {
        "is_ipv4", ipdb_is_support_ipv4, METH_NOARGS,
        "Get support IPv4."
    },
    {
        "is_ipv6", ipdb_is_support_ipv6, METH_NOARGS,
        "Get support IPv6."
    },
    {
        "build_time", ipdb_build_time, METH_NOARGS,
        "Get build time."
    },
    {NULL, NULL, 0, NULL}
};

static PyObject *
ipdb_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
    PyIPDB_Object *ps;
    ps = (PyIPDB_Object *) type->tp_alloc(type, 0);
    if (ps == NULL) return NULL;

    if (!PyArg_ParseTuple(args, "s", &ps->path)) {
        return NULL;
    }

    int err = ipdb_reader_new(ps->path, &ps->reader);
    if (err)
    {
        PyErr_SetString(PyExc_TypeError,
                        "Can't load ipip.net library, read error");
        return NULL;
    }

    ps->fields = calloc(sizeof(PyObject *), ps->reader->meta->fields_length);
    for (int i = 0; i < ps->reader->meta->fields_length; ++i) {
        ps->fields[i] = PyUnicode_FromString(ps->reader->meta->fields[i]);
    }

    return (PyObject *) ps;
}

static PyTypeObject IPDBType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "ipdb.City",
    .tp_doc = "IPDB.net IP Resolve objects",
    .tp_basicsize = sizeof(PyIPDB_Object),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_methods = ipdb_methods,
    .tp_new = ipdb_new,
};

// Module definition
// The arguments of this structure tell Python what to call your extension,
// what it's methods are and where to look for it's method definitions
static struct PyModuleDef ipdb_definition = { 
    PyModuleDef_HEAD_INIT,
    "ipdb",
    "A Python module that prints 'hello world' from C code.",
    -1, 
    NULL
};

// Module initialization
// Python calls this function when importing your extension. It is important
// that this function is named PyInit_[[your_module_name]] exactly, and matches
// the name keyword argument in setup.py's setup() call.
PyMODINIT_FUNC PyInit_ipdb(void) {
    PyObject *m;
    if (PyType_Ready(&IPDBType) < 0)
        return NULL;

    m = PyModule_Create(&ipdb_definition);
    if (m == NULL)
        return NULL;

    Py_INCREF(&IPDBType);
    if (PyModule_AddObject(m, "City", (PyObject *) &IPDBType) < 0) {
        Py_DECREF(&IPDBType);
        Py_DECREF(m);
        return NULL;
    }

    return m;
}
