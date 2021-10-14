import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8258"
version_tuple = (0, 0, 8258)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8258")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8146"
data_version_tuple = (0, 0, 8146)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8146")
except ImportError:
    pass
data_git_hash = "4a8e2ce55209660d86d89f4cb054165a362292b8"
data_git_describe = "v0.0-8146-g4a8e2ce55"
data_git_msg = """\
commit 4a8e2ce55209660d86d89f4cb054165a362292b8
Author: Timothy Trippel <ttrippel@google.com>
Date:   Wed Oct 6 00:19:34 2021 +0000

    [dif/aon_timer] Integrate autogen'd IRQ DIFs into test code.
    
    This commit partially addresses #8142. Specifically it:
    1. deprecates existing (manually implemented) **Always-On Timer** IRQ DIFs,
    2. integrates the auto-generated **Always-On Timer** IRQ DIFs into meson build
       targets, and
    3. refactors all existing source code to make use of the new auto-genenerated
       **Always-On Timer** IRQ DIFs, and supporting shared DIF typedefs and
       error codes.
    
    This continues the long-term goal of auto-generating all IRQ DIFs across
    all IPs, as described in #8142.
    
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
