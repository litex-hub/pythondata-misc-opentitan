import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5432"
version_tuple = (0, 0, 5432)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5432")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5337"
data_version_tuple = (0, 0, 5337)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5337")
except ImportError:
    pass
data_git_hash = "55a311a1dc9e423986d47d1927e74fb518c95aed"
data_git_describe = "v0.0-5337-g55a311a1d"
data_git_msg = """\
commit 55a311a1dc9e423986d47d1927e74fb518c95aed
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Wed Mar 17 15:34:51 2021 +0000

    [util] Don't explode on unexpected format in fix_include_guard.py
    
    The existing code assumed that there was an #ifndef line somewhere in
    the file and exploded if not (calling None.group()). This patch
    handles these cases more gracefully by having a notion of "unfixable"
    files. It also changes the output format a bit to make the CI
    wrapper's job a bit easier.
    
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
