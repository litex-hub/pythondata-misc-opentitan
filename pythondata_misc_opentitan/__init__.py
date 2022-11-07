import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15271"
version_tuple = (0, 0, 15271)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15271")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15129"
data_version_tuple = (0, 0, 15129)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15129")
except ImportError:
    pass
data_git_hash = "db60a6ae14e1186afddd7e114986cd65f87fad79"
data_git_describe = "v0.0-15129-gdb60a6ae14"
data_git_msg = """\
commit db60a6ae14e1186afddd7e114986cd65f87fad79
Author: Alexander Williams <awill@google.com>
Date:   Fri Oct 28 10:15:04 2022 -0700

    [top_earlgrey/dv] Add filtering variant of SPI passthrough test
    
    Add variant of SPI passthrough test that incorporates the use of
    filtered opcodes.
    
    Signed-off-by: Alexander Williams <awill@google.com>

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
