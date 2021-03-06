import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5268"
version_tuple = (0, 0, 5268)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5268")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5173"
data_version_tuple = (0, 0, 5173)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5173")
except ImportError:
    pass
data_git_hash = "6c72d84e37b0d790dd4793c5b3919ab9e02d215b"
data_git_describe = "v0.0-5173-g6c72d84e3"
data_git_msg = """\
commit 6c72d84e37b0d790dd4793c5b3919ab9e02d215b
Author: Timothy Chen <timothytim@google.com>
Date:   Fri Mar 5 16:53:19 2021 -0800

    [util] Slight refactor of secded_gen.py
    
    - list all secded flavors in util/design/data/secded_cfg.hjson
    - generate single package file for portable re-use
    - nothing else is touched
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
