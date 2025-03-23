print("running __init__.py")
try:
    from ._version import version
except ModuleNotFoundError:
    version = 'no_version'



