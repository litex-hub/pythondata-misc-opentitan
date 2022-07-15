import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13128"
version_tuple = (0, 0, 13128)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13128")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12986"
data_version_tuple = (0, 0, 12986)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12986")
except ImportError:
    pass
data_git_hash = "2b989a42bad3aff373e024ce841b406eec1b3970"
data_git_describe = "v0.0-12986-g2b989a42ba"
data_git_msg = """\
commit 2b989a42bad3aff373e024ce841b406eec1b3970
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Fri Jul 15 13:34:28 2022 -0700

    fix(cdc): Parse NEW violations only
    
    This commit revises the CDC flow to parse NEW report not ALL report
    file. The result report contains only NEW violations. Previously, the
    report has WAIVED list too.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

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
