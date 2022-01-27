import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9830"
version_tuple = (0, 0, 9830)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9830")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9708"
data_version_tuple = (0, 0, 9708)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9708")
except ImportError:
    pass
data_git_hash = "b20f5d5f803cbb89227dd3fc57eadd989cdf0ac0"
data_git_describe = "v0.0-9708-gb20f5d5f8"
data_git_msg = """\
commit b20f5d5f803cbb89227dd3fc57eadd989cdf0ac0
Author: Michael Schaffner <msf@opentitan.org>
Date:   Wed Jan 26 16:31:45 2022 -0800

    [pinmux/doc] Fix a TODO in the docs
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
