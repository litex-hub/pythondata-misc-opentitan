import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14483"
version_tuple = (0, 0, 14483)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14483")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14341"
data_version_tuple = (0, 0, 14341)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14341")
except ImportError:
    pass
data_git_hash = "befa83b43297b2764af9d2be93a761b41e255286"
data_git_describe = "v0.0-14341-gbefa83b432"
data_git_msg = """\
commit befa83b43297b2764af9d2be93a761b41e255286
Author: Jade Philipoom <jadep@google.com>
Date:   Tue Sep 27 13:36:05 2022 +0200

    [doc] Cleanup and fixes for install guide.
    
    Adjust the install guide pages based on feedback and on a read-through:
    - Reverses the order of the Verilator install and the software build,
      since Bazel tests essentially require Verilator
    - Changes the tl;dr section of the software build page to something that
      should succeed on the first try (the previous example required
    Verible)
    - Adds troubleshooting notes and information about RAM requirements
    - Adds notes and time estimates for long-running steps
    - Updates information about the CI setup (we now use Ubuntu 20.04, not
      18.04)
    - Removes "$" before console commands to make them easier to copy-paste
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

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
