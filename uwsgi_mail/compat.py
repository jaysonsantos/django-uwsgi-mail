try:
    from cPickle import dumps, loads  # noqa
except ImportError:
    from pickle import dumps, loads  # noqa

try:
    from uwsgidecorators import spool
except ImportError:
    import warnings
    warnings.warn("You are using this module outside of uwsgi make sure it is running your app.")

    def spool(f):
        return f


__all__ = ('dumps', 'loads', 'spool')
