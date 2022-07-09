import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13005"
version_tuple = (0, 0, 13005)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13005")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12863"
data_version_tuple = (0, 0, 12863)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12863")
except ImportError:
    pass
data_git_hash = "3da5eab1ed884a516c35cca5db182e0ad0acb024"
data_git_describe = "v0.0-12863-g3da5eab1ed"
data_git_msg = """\
commit 3da5eab1ed884a516c35cca5db182e0ad0acb024
Author: Dan McArdle <dmcardle@google.com>
Date:   Wed Jun 29 15:45:14 2022 -0400

    [util/design] Generate MEM instead of hexfile in gen-otp-img.py
    
    See lowRISC/OpenTitan#10867
    
    Signed-off-by: Dan McArdle <dmcardle@google.com>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
