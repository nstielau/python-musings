def print_function(*args, **kwargs):
    print "I am in print function"
    print args

try:
    from clint.textui import colored, indent, puts
except Exception as e:
    print "Caught exception: {0}".format(e)
    puts = print_function

puts('this is stuff')
