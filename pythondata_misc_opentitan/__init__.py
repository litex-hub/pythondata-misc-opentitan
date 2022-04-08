import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11476"
version_tuple = (0, 0, 11476)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11476")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11350"
data_version_tuple = (0, 0, 11350)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11350")
except ImportError:
    pass
data_git_hash = "876de558dc1e58d00c7742bb25e115ca23f96096"
data_git_describe = "v0.0-11350-g876de558d"
data_git_msg = """\
commit 876de558dc1e58d00c7742bb25e115ca23f96096
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Fri Apr 8 00:29:43 2022 -0700

    [chip dv] Fix coverage collection for chip XBAR tests
    
    The coverage on all functional hierarchies were inadvertantly
    being collected on chip level XBAR tests, which are supposed to
    stub all TL hosts and devices. This was causing a larger coverge
    numbers to be reported than intended. This commit fixes that.
    
    We add ` xbar_build_mode` as a replacement for the `default` build
    mode. This is done so, so that the chip level testbench which
    reuses XBAR tests can append / override `xbar_build_mode` with
    additional build-time settings. We use this method to specify
    the right coverage collection hierarchy file for the XBAR tests.
    This coverage collection hierarchy file is the same one as the one
    use for the chip level `cover_reg_top` build mode - which restricts
    the coverage collection only to TL interfaces on all hosts and
    devices.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
