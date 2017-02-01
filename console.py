from code import compile_command
import sys
import traceback


def interact(locals_, target):
    while True:
        try:
            buffer = []
            line = input('>>> ')

            while True:
                buffer.append(line)
                source = '\n'.join(buffer)
                if run_source(source, locals_):
                    break

                line = input('... ')

            try:
                if eval('_') == target:
                    return
            except NameError:
                pass

        except EOFError:
            print()
            break
        except KeyboardInterrupt:
            print('\nKeyboardInterrupt')

def run_source(source, locals_):
    try:
        code = compile_command(source, '<console>', 'single')
    except (OverflowError, SyntaxError, ValueError):
        show_syntax_error()
        return True

    if code is None:
        return False

    try:
        exec(code, locals_)
    except SystemExit:
        raise
    except:
        show_traceback()

    return True

def show_syntax_error():
    etype, value, tb = sys.exc_info()
    lines = traceback.format_exception_only(etype, value)
    print(''.join(lines))

def show_traceback():
    etype, value, tb = sys.exc_info()
    lines = traceback.format_exception(etype, value, tb.tb_next)
    print(''.join(lines))
