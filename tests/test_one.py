import eztest

def test_one():

    def func2(x):
        return x * 2

    def func3(x):
        return x * 3

    def func1(x):
        return func2(x) + func3(x)

    eztest.tc(func1)(2)

    print(eztest.gen_tests())

    assert eztest.gen_tests() == '\ndef test_func1():\n    assert func1(x=2) == 10\n\ndef test_func2():\n    assert func2(x=2) == 4\n\ndef test_func3():\n    assert func3(x=2) == 6\n'

