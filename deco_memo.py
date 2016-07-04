def decoration(func):
    def wrapper(name):
        print "a"
        func(name)
        print "c"
    return wrapper


@decoration
def foo(name):
    print name

foo('sonite')
