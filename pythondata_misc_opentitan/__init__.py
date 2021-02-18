import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5042"
version_tuple = (0, 0, 5042)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5042")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4951"
data_version_tuple = (0, 0, 4951)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4951")
except ImportError:
    pass
data_git_hash = "789ea02bbe3a60c883e25a1cfa2f8d50a950ac43"
data_git_describe = "v0.0-4951-g789ea02bb"
data_git_msg = """\
commit 789ea02bbe3a60c883e25a1cfa2f8d50a950ac43
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Fri Feb 12 14:35:42 2021 -0800

    [entropy_src/rtl] add fatal alert
    
    ERR_CODE is RO and can be tested with a register.
    Re-ran top level to make updates to interconnections.
    Re-ran the reg script.
    Re-ran top level again.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
