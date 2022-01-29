import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9914"
version_tuple = (0, 0, 9914)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9914")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9790"
data_version_tuple = (0, 0, 9790)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9790")
except ImportError:
    pass
data_git_hash = "72e83f01dbfda68f3473c3efc97a54d6bf0950c7"
data_git_describe = "v0.0-9790-g72e83f01d"
data_git_msg = """\
commit 72e83f01dbfda68f3473c3efc97a54d6bf0950c7
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Fri Jan 28 07:49:48 2022 -0800

    [edn/rtl] D2S review updates
    
    Feedback from the D2S review reflected back into the design.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
