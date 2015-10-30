import sys

def exc_hook(*args):
    print 'Unhandled portal_jobs {typ} exception: {exc_info}'.format(
        typ=args[0].__name__,
        exc_info=args
    )

    sys.__excepthook__(*args)

sys.excepthook = exc_hook
raise Exception('asdf')
