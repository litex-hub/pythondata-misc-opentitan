import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15096"
version_tuple = (0, 0, 15096)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15096")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14954"
data_version_tuple = (0, 0, 14954)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14954")
except ImportError:
    pass
data_git_hash = "27c13f095112b2621e2a9e7fb784dc23b7c73485"
data_git_describe = "v0.0-14954-g27c13f0951"
data_git_msg = """\
commit 27c13f095112b2621e2a9e7fb784dc23b7c73485
Author: Vladimir Rozic <vrozic@lowrisc.org>
Date:   Tue Nov 1 15:47:34 2022 +0000

    [python] Removing numpy from the python requirements
    
    Removing numpy from python-requirements.txt as it is not currently
    used.
    
    Signed-off-by: Vladimir Rozic <vrozic@lowrisc.org>

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
