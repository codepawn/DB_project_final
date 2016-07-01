
def db_commit_decorate(func):
    def wrapper(name):
        print "A"
        func(name)
        print "C"
    return wrapper


@db_commit_decorate
def commit(name):
    print(name)

commit('foo')


def a():
    a = "a"
    return a


def b():
    print a()

b()
