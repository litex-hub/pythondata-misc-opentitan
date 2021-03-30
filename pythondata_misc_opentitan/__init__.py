import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5629"
version_tuple = (0, 0, 5629)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5629")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5534"
data_version_tuple = (0, 0, 5534)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5534")
except ImportError:
    pass
data_git_hash = "c658d4ee08be6a20c9925f1013346777fe1a7f21"
data_git_describe = "v0.0-5534-gc658d4ee0"
data_git_msg = """\
commit c658d4ee08be6a20c9925f1013346777fe1a7f21
Author: Philipp Wagner <phw@lowrisc.org>
Date:   Wed Mar 24 14:43:11 2021 +0000

    [dif_alert_handler] Use auto-generated Hjson file
    
    The alert_handler is an IP template which is instantiated with a
    top_earlgrey-specific configuration. The C header file must be generated
    from the templated Hjson file, not the example Hjson file which happens
    to be in the tree as well, but doesn't contain the right configuration.
    
    Fixes #5778
    
    Signed-off-by: Philipp Wagner <phw@lowrisc.org>

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
