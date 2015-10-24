

def a(param={}):
   print str(param)
   param['bobo'] = True
   return param

print 'Running a for the first time, expecting default param'
a()
print "Running a() again, expect default param"
a()
print "But getting some bobocity"
