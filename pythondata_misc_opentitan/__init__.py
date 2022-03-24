import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11117"
version_tuple = (0, 0, 11117)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11117")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10991"
data_version_tuple = (0, 0, 10991)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10991")
except ImportError:
    pass
data_git_hash = "ba061ed571068884e7f9d7bc10d30cbb8dd4ebf9"
data_git_describe = "v0.0-10991-gba061ed57"
data_git_msg = """\
commit ba061ed571068884e7f9d7bc10d30cbb8dd4ebf9
Author: Timothy Trippel <ttrippel@google.com>
Date:   Wed Mar 23 00:30:22 2022 -0700

    [bazel] Add rules to generate SPI Flash frames for DV bootstrap
    
    DV simulations can load the flash either via backdoor memory write, or
    bootstrap. If via bootstrap, a special image must be prepared so that
    the test bench can feed the correct SPI flash frames to the DUT. This
    commit adds custom bazel rules to generate this flash image.
    
    This partially addresses #11559.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
