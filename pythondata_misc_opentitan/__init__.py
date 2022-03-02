import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10640"
version_tuple = (0, 0, 10640)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10640")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10514"
data_version_tuple = (0, 0, 10514)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10514")
except ImportError:
    pass
data_git_hash = "d953b0ca0f734798979d5d24d37f27164a4cf1be"
data_git_describe = "v0.0-10514-gd953b0ca0"
data_git_msg = """\
commit d953b0ca0f734798979d5d24d37f27164a4cf1be
Author: Timothy Trippel <ttrippel@google.com>
Date:   Fri Feb 25 17:41:50 2022 -0800

    [dif/pwm] Add autogen, header, and checklist
    
    This adds part of the DIF library for the PWM, including:
    1. all autogenerated DIFs,
    2. a header with a suggested API,
    3. a checklist.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
