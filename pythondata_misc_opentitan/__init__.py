import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12670"
version_tuple = (0, 0, 12670)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12670")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12528"
data_version_tuple = (0, 0, 12528)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12528")
except ImportError:
    pass
data_git_hash = "71d4a19ac81f137a304a00a7c550d2ddc6c60fa9"
data_git_describe = "v0.0-12528-g71d4a19ac"
data_git_msg = """\
commit 71d4a19ac81f137a304a00a7c550d2ddc6c60fa9
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Mon Jun 13 16:58:31 2022 +0200

    [fpga] Make `set_clock_sense` constraint more flexible using a wildcard
    
    It seems that the name of the target LUT cell may change as the
    design evolves. This results in Vivado not being able to apply the
    constraint and triggering a critical warning instead.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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
