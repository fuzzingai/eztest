import sys

from IPython.core.debugger import set_trace

# Initialize a dictionary to hold function arguments and results
call_cache = {}

# Define a trace function
def trace_call_cb(frame, event, arg):
    global call_cache
    code = frame.f_code
    func_name = code.co_name
    if event == 'call':
        call_cache[func_name] = {
            "args": frame.f_locals,
            "result": None  # We don't know the result yet
        }

        return trace_call_cb
    elif event == 'return':
        call_cache[func_name]['result'] = arg


def tc(func):
    global call_cache
    call_cache = {}
    def meh(*args, **kwargs):
        sys.settrace(trace_call_cb)
        func(*args, **kwargs)
        sys.settrace(None)
    return meh


def gen_tests():
    global call_cache
    buf = ""

    for func, cache in call_cache.items():
        args = ', '.join(f"{k}={v!r}" for k, v in cache['args'].items())
        buf += f"""
def test_{func}():
    assert {func}({args}) == {cache['result']}\n"""

    return buf
