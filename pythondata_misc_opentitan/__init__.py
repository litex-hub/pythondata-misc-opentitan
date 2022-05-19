import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12236"
version_tuple = (0, 0, 12236)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12236")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12108"
data_version_tuple = (0, 0, 12108)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12108")
except ImportError:
    pass
data_git_hash = "605d0bd56d559d248f2dd5314d8845715e7981f7"
data_git_describe = "v0.0-12108-g605d0bd56"
data_git_msg = """\
commit 605d0bd56d559d248f2dd5314d8845715e7981f7
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Wed May 18 17:56:19 2022 -0700

    [dv/pattgen] Modify coverage exclusions
    
    This is discussed in issue #12545.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post128"
tool_version_tuple = (0, 0, 128)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post128")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
