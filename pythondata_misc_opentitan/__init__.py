import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8166"
version_tuple = (0, 0, 8166)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8166")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8054"
data_version_tuple = (0, 0, 8054)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8054")
except ImportError:
    pass
data_git_hash = "eb29bdb3aeacbf693df70c0063c869b044237f13"
data_git_describe = "v0.0-8054-geb29bdb3a"
data_git_msg = """\
commit eb29bdb3aeacbf693df70c0063c869b044237f13
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Wed Sep 29 11:30:07 2021 +0100

    [otbn] Prevent RF integrity error when there is a call stack error
    
    When a call stack pop causes an underflow both integrity and data bits
    are invalid so the integrity error has no meaning.
    
    Fixes #8354
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
