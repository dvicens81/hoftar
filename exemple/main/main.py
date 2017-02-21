import re
var = raw_input("Please enter a array (Ex: 123433245): ")

regex = r"134"
compiled_re = re.compile(regex)
res = compiled_re.search(var)
if res is not None:
    print 'Found it %s ' % var
else:
    print 'Not found in %s ' % var