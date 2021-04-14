import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5865"
version_tuple = (0, 0, 5865)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5865")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5770"
data_version_tuple = (0, 0, 5770)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5770")
except ImportError:
    pass
data_git_hash = "952b714368b8af072c7b3376c9f593633c72a157"
data_git_describe = "v0.0-5770-g952b71436"
data_git_msg = """\
commit 952b714368b8af072c7b3376c9f593633c72a157
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Wed Apr 14 13:51:33 2021 +0100

    [otbn,dv] Use "done" directly in the idle checker module
    
    We were reconstructing "done" by looking at the hw2reg signals. This
    is sort of nice, because you can do it by just looking at OTBN's
    output ports. Unfortunately, it doesn't quite work because these
    signals are also triggered by writes to the INTR_TEST register.
    
    Since we're binding otbn_idle_checker into otbn anyway, just snoop on
    the internal "done" signal that we actually want.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
