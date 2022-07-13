import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13058"
version_tuple = (0, 0, 13058)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13058")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12916"
data_version_tuple = (0, 0, 12916)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12916")
except ImportError:
    pass
data_git_hash = "0b3a704ea86aafab27133a5bd2cad6359cd302e9"
data_git_describe = "v0.0-12916-g0b3a704ea8"
data_git_msg = """\
commit 0b3a704ea86aafab27133a5bd2cad6359cd302e9
Author: Drew Macrae <drewmacrae@google.com>
Date:   Fri Jul 1 12:41:23 2022 -0400

    [build] clean up old mentions of meson
    
    * In BUILD.bazel we mention meson and want to preserve the structure for
    other reasons
    * Update OpenTitan's riscv_compliance patches to describe how we now run
      them
    
    Signed-off-by: Drew Macrae <drewmacrae@google.com>

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
