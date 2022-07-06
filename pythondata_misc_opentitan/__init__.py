import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12941"
version_tuple = (0, 0, 12941)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12941")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12799"
data_version_tuple = (0, 0, 12799)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12799")
except ImportError:
    pass
data_git_hash = "9ae5ae66bd43388105d1874bf26e6dc41eb5c4ad"
data_git_describe = "v0.0-12799-g9ae5ae66bd"
data_git_msg = """\
commit 9ae5ae66bd43388105d1874bf26e6dc41eb5c4ad
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Wed Jun 22 13:32:45 2022 +0000

    [dv,flash_ctrl] Add more scramble test
    
    - Change ditribution of the number of ctrl req
    - Add small word test
    
    Signed-off-by: Jaedon Kim <jdonjdon@google.com>

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
