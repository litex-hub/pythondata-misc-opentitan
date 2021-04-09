import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5799"
version_tuple = (0, 0, 5799)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5799")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5704"
data_version_tuple = (0, 0, 5704)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5704")
except ImportError:
    pass
data_git_hash = "2d1514875d58abf19939ba1432ddc5006f7f282c"
data_git_describe = "v0.0-5704-g2d1514875"
data_git_msg = """\
commit 2d1514875d58abf19939ba1432ddc5006f7f282c
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Wed Apr 7 13:27:48 2021 +0100

    [alert,lint] Add explicit cast for comparison in ping timer
    
    This cast is safe because IdDw is $clog2(NAlerts + N_ESC_SEV) and
    N_ESC_SEV (the number of escalation severities, defined in the hjson)
    is positive.
    
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
