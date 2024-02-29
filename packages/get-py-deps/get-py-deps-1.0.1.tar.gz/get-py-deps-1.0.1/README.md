# get-py-deps

A Python module to pretty print a table with the dependencies of a Python package with license and url.

Can both be used in your code with `from get_py_deps import get_py_deps` or as a command line tool as.

```bash
$ get_py_deps sphinx
```

Which will output a table with the licenses and urls which were found as dependencies to that package.

```bash
+--------------------------------------+--------------------------------------------------------------+-------------------------------------------+
|               Package                |                           License                            |                    Url                    |
+--------------------------------------+--------------------------------------------------------------+-------------------------------------------+
|           alabaster 0.7.16           |                     (License not found)                      |            (Homepage not found)           |
|           docutils 0.17.1            | public domain, Python, 2-Clause BSD, GPL 3 (see COPYING.txt) |      http://docutils.sourceforge.net/     |
|           imagesize 1.4.1            |                             MIT                              | https://github.com/shibukawa/imagesize_py |
|             Jinja2 3.1.3             |                         BSD-3-Clause                         |    https://palletsprojects.com/p/jinja/   |
|            packaging 23.2            |                     (License not found)                      |            (Homepage not found)           |
|           requests 2.31.0            |                          Apache 2.0                          |      https://requests.readthedocs.io      |
|        snowballstemmer 2.2.0         |                         BSD-3-Clause                         |  https://github.com/snowballstem/snowball |
|    sphinxcontrib-applehelp 1.0.8     |                     (License not found)                      |            (Homepage not found)           |
|     sphinxcontrib-devhelp 1.0.6      |                     (License not found)                      |            (Homepage not found)           |
|     sphinxcontrib-htmlhelp 2.0.5     |                     (License not found)                      |            (Homepage not found)           |
|      sphinxcontrib-jsmath 1.0.1      |                             BSD                              |           http://sphinx-doc.org/          |
|      sphinxcontrib-qthelp 1.0.7      |                     (License not found)                      |            (Homepage not found)           |
| sphinxcontrib-serializinghtml 1.1.10 |                     (License not found)                      |            (Homepage not found)           |
+--------------------------------------+--------------------------------------------------------------+-------------------------------------------+
```

Note that the package and its dependencies needs to be installed in the environment where the command is run.

Use case could be that you want to add an option to your own CLI tool to list the dependencies of your tool.

<p>
  <h1 align="right"><b>🦆<img src="" alt="" width="100"></h1>
</p>
