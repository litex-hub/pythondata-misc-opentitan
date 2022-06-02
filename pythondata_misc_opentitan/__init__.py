import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12473"
version_tuple = (0, 0, 12473)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12473")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12331"
data_version_tuple = (0, 0, 12331)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12331")
except ImportError:
    pass
data_git_hash = "6f05ffc3ffa9ca2604e46d9538eb0f5211fe4799"
data_git_describe = "v0.0-12331-g6f05ffc3f"
data_git_msg = """\
commit 6f05ffc3ffa9ca2604e46d9538eb0f5211fe4799
Author: Miles Dai <milesdai@google.com>
Date:   Tue May 31 13:01:07 2022 -0400

    [ci] Clean up verilator chip-level testing configuration.
    
    This commit undoes the temporary actions in #12603 that were taken to
    prevent blocking on the Verilator chip-level tests back when these tests
    were flaky.
    
    Signed-off-by: Miles Dai <milesdai@google.com>

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
