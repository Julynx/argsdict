import sys


def args(positional=None):
    """
    Simple command-line argument parser.

    Args:
        positional (list): List of names for arguments based on their position.

    Returns:
        dict: Dictionary of argument names and values.
              Regular arguments are named according to their position and
              mapped to their values. Flags are also mapped to their
              values (--flag=value) or to True if no value is specified.

    Usage:
        $ python args.py John Smith --age=30 --married

        arg = args(["name", "surname"])
        >> {"name": "John",
            "surname": "Smith",
            "--age": "30",
            "--married": True}
    """
    def _split_flag(arg_name):
        if "=" in arg_name:
            return arg_name.split("=", maxsplit=1)
        return arg_name, True

    if positional is None:
        positional = []

    flags = [arg
             for arg in sys.argv[1:]
             if arg.startswith('-')]

    non_flags = [arg
                 for arg in sys.argv[1:]
                 if not arg.startswith('-')]

    return dict(zip(positional, non_flags)) | dict(map(_split_flag, flags))
