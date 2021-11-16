import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8738"
version_tuple = (0, 0, 8738)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8738")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8626"
data_version_tuple = (0, 0, 8626)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8626")
except ImportError:
    pass
data_git_hash = "84291ebf7c2a740ffdd4954de05431facbd63369"
data_git_describe = "v0.0-8626-g84291ebf7"
data_git_msg = """\
commit 84291ebf7c2a740ffdd4954de05431facbd63369
Author: Timothy Trippel <ttrippel@google.com>
Date:   Sat Nov 13 00:53:30 2021 +0000

    [sw/ottf] Restructure meson build targets for OTTF.
    
    For testing the OTTF, a single meson build target was constructed with
    an example test built in. This refactors the build targets to build the
    OTTF as a library that is linked with tests that are also defined as
    libraries. This makes building test binaries that use the OTTF similar
    to those that use the existing test_main.c test framework.
    
    Additionally, two example OTTF tests (one bare-metal and one concurrency)
    are added to provided examples of how to write on-device tests using the
    OTTF.
    
    This partially addresses a larger effort of refactoring the on-device
    test framework, as described in #8015.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
