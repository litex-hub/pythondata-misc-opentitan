import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9753"
version_tuple = (0, 0, 9753)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9753")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9631"
data_version_tuple = (0, 0, 9631)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9631")
except ImportError:
    pass
data_git_hash = "dc15a395a70512b74dc56a4d2839db7fe1784a3b"
data_git_describe = "v0.0-9631-gdc15a395a"
data_git_msg = """\
commit dc15a395a70512b74dc56a4d2839db7fe1784a3b
Author: Drew Macrae <drewmacrae@google.com>
Date:   Mon Jan 24 14:36:10 2022 -0800

    [bazel] fixup #10041 conflict
    
    it looks like we see a conflict in CI between
    https://github.com/lowRISC/opentitan/pull/10041 and
    https://github.com/lowRISC/opentitan/pull/10148
    
    this should resolve it and I've tested by building on my workstation
    
    Signed-off-by: Drew Macrae <drewmacrae@google.com>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
