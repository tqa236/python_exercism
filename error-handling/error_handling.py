"""Practice handling various kind of errors."""


def handle_error_by_throwing_exception():
    """Throw exception."""
    raise ValueError("No input")


def handle_error_by_returning_none(input_data):
    """Return None if errors."""
    try:
        return int(input_data)
    except ValueError:
        return None


def handle_error_by_returning_tuple(input_data):
    """Return the result and the status."""
    try:
        return True, int(input_data)
    except ValueError:
        return False, input_data


def filelike_objects_are_closed_on_exception(filelike_object):
    """Catch exception of an object."""
    try:
        filelike_object.open()
        filelike_object.do_something()
    except Exception:
        raise Exception("Error! Close filelike_object.")
    finally:
        filelike_object.close()
