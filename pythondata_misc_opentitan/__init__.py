import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9522"
version_tuple = (0, 0, 9522)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9522")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9400"
data_version_tuple = (0, 0, 9400)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9400")
except ImportError:
    pass
data_git_hash = "28deecfe0b680203aefceb143b7ade77a2570d44"
data_git_describe = "v0.0-9400-g28deecfe0"
data_git_msg = """\
commit 28deecfe0b680203aefceb143b7ade77a2570d44
Author: Timothy Chen <timothytim@google.com>
Date:   Wed Jan 12 16:36:54 2022 -0800

    [doc] update tlul and flash documentation
    
    - update to explain instruction type attribute in tlul user bits.
    - update to explain how flash execution contro makes use of the
      instruction type bits.
    
    - Companion PR to #10035 and #10022
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
