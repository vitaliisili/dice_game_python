from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("baboo_game")
except PackageNotFoundError:
    pass
