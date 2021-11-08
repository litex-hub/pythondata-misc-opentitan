import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8634"
version_tuple = (0, 0, 8634)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8634")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8522"
data_version_tuple = (0, 0, 8522)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8522")
except ImportError:
    pass
data_git_hash = "af4c9e7168d15a164b473b5f4d0a377791facf7d"
data_git_describe = "v0.0-8522-gaf4c9e716"
data_git_msg = """\
commit af4c9e7168d15a164b473b5f4d0a377791facf7d
Author: Drew Macrae <drewmacrae@google.com>
Date:   Wed Nov 3 02:15:05 2021 +0000

    [bazel] add rules for new targets and fix unittest
    
    building with bazel I came across a few issues
    * remove an included header that's only implemented for riscv targets
    from the dif_aes_unittest
    * added a freestanding library
    * ran buildifier which caught a late change I missed on my last bazel
    commit
    * included stdint in a couple header files that use it.
    
    Signed-off-by: Drew Macrae <drewmacrae@google.com>

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
