PyElb - Py Elastic Load Balancer Log Parser
===========================================

PyElb is a tool to parse and print log files generated by the Amazon Electic Load Balancer

How to install it?
-----------------------
You can install it with pip doing the following:

    $ pip install -e git+https://github.com/carrerasrodrigo/pyelb.git#egg=pyelb

or you can clone this repository and install it.

    $ git clone https://github.com/carrerasrodrigo/pyelb.git
    $ cd pyelb
    $ python setup.py install


How to run it?
-----------------------


### Basic Example

```python
pyelb --file=PATH_TO_LOG_FILE
```

### Limit the number of lines to print

```python
pyelb --file=PATH_TO_LOG_FILE --limit=10 --offset=2
```

### Order the information

```python
pyelb --file=PATH_TO_LOG_FILE --limit=10 --offset=2 --order=COL_NAME
```

or ordering the other way around:
```python
pyelb --file=PATH_TO_LOG_FILE --limit=10 --offset=2 --order-reverse=COL_NAME
```

### Print an specific list of columns

```python
pyelb --file=PATH_TO_LOG_FILE --limit=10 --offset=2 --order=COL_NAME --col=request,request_processing_time
```

if you want to see the full list of columns available, run the following command:
```python
pyelb --print-valid-columns=1
```

There are two special columns that are added automatically by pyelb: all and  total_processing_time.
```
total_processing_time = request_processing_time + backend_processing_time + response_processing_time
all = all available columns
```

### Tested on

This project has been tested on Python 2.7+ and Python 3.4+
