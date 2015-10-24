to_find = "rew"
string = "rerewhatregweetere"
print "Looking for {} in {}".format(to_find, string)
for i in range(len(string)):
    print "Examining: {}".format(string[i])
    for j in range(len(to_find)):
        if len(string) <= i+j:
            break
        if string[i+j] != to_find[j]:
            break
        if j + 1 == len(to_find):
            print "Found another '%s'" % to_find
