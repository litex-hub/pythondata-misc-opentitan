import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10600"
version_tuple = (0, 0, 10600)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10600")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10474"
data_version_tuple = (0, 0, 10474)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10474")
except ImportError:
    pass
data_git_hash = "c4eb9a456c28fd6c5fabec293a908cfa2ba73022"
data_git_describe = "v0.0-10474-gc4eb9a456"
data_git_msg = """\
commit c4eb9a456c28fd6c5fabec293a908cfa2ba73022
Author: Alexander Williams <awill@google.com>
Date:   Wed Feb 16 08:30:19 2022 -0800

    [usbdev] Clean up confusing uses of "differential"
    
    Explicitly refer to a receiver wherever "differential" is used with
    "rx".
    
    Previously, the term on RX would mean that an *external* differential
    receiver would be used, delivering a *single-ended* data signal to the
    IP. However, this top-level definition causes too much confusion.
    
    Similarly, for TX, avoid using "differential" altogether, as neither the
    driver nor the signals are truly differential. Instead, refer to the two
    interfaces by the component signal names.
    
    Signed-off-by: Alexander Williams <awill@google.com>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
