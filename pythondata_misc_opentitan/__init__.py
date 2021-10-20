import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8351"
version_tuple = (0, 0, 8351)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8351")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8239"
data_version_tuple = (0, 0, 8239)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8239")
except ImportError:
    pass
data_git_hash = "1b6cc1e09710abc88e0a7a6e67a106d508e28cf2"
data_git_describe = "v0.0-8239-g1b6cc1e09"
data_git_msg = """\
commit 1b6cc1e09710abc88e0a7a6e67a106d508e28cf2
Author: Timothy Trippel <ttrippel@google.com>
Date:   Tue Oct 19 05:43:05 2021 +0000

    [dif/rv_timer] Integrate autogen'd DIF artifacts into src tree.
    
    This commit partially addresses #8142. Specifically it:
    1. deprecates existing (manually implemented) **RV Timer**
       specific DIF return codes, toggle types, and params,
    2. integrates the auto-generated **RV Timer** DIFs into meson build
       targets,
    3. refactors all existing source code to make use of the new shared DIF
       types and error codes, and
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
