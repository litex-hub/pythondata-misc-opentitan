import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8843"
version_tuple = (0, 0, 8843)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8843")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8731"
data_version_tuple = (0, 0, 8731)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8731")
except ImportError:
    pass
data_git_hash = "7a4fc2933ca3b54a2942c2b727adcdd415baec79"
data_git_describe = "v0.0-8731-g7a4fc2933"
data_git_msg = """\
commit 7a4fc2933ca3b54a2942c2b727adcdd415baec79
Author: Timothy Trippel <ttrippel@google.com>
Date:   Tue Nov 23 00:58:19 2021 +0000

    [sw/ottf] Rename OTTF exception handlers.
    
    This commit adds the suffix `_handler` to each default exception
    handling function that is invoked by the main OTTF exception handler.
    
    Additionally, this commit makes the main OTTF exection handler a strong
    symbol, since test developers that use the OTTF should override the
    appropriate OTTF exception handler function for the functionality they
    are trying to test.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
