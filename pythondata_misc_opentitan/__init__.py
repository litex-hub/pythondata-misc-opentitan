import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8305"
version_tuple = (0, 0, 8305)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8305")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8193"
data_version_tuple = (0, 0, 8193)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8193")
except ImportError:
    pass
data_git_hash = "18dc61a53ea9d46a34fabee933067b243812e783"
data_git_describe = "v0.0-8193-g18dc61a53"
data_git_msg = """\
commit 18dc61a53ea9d46a34fabee933067b243812e783
Author: Miguel Osorio <miguelosorio@google.com>
Date:   Thu Oct 14 10:39:58 2021 -0700

    [hw/rom] Increase ROM size to 32kB.
    
    Increase mask ROM to 32kB to allow the mask ROM development to continue
    before we start size optimizations.
    
    Even though the mask ROM size may potentially fit within 16kB, it is
    safer to preallocate additional space while we iterate over countermeasures
    and final feature set.
    
    Signed-off-by: Miguel Osorio <miguelosorio@google.com>

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
