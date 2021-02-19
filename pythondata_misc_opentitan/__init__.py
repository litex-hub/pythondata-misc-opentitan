import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5061"
version_tuple = (0, 0, 5061)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5061")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4970"
data_version_tuple = (0, 0, 4970)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4970")
except ImportError:
    pass
data_git_hash = "b40383473ca14e7b352be7b150afbf26d362a4b9"
data_git_describe = "v0.0-4970-gb40383473"
data_git_msg = """\
commit b40383473ca14e7b352be7b150afbf26d362a4b9
Author: Michael Schaffner <msf@google.com>
Date:   Wed Feb 17 21:47:34 2021 -0800

    [dvsim/syn] Update parsing script and area reporting
    
    This updates the area reporting of the DVSIM parser script.
    Submodules can now be expanded recursively by name, or by
    setting a maximum expansion depth. This allows us for instance
    to report two levels of hierarchy, where we only expand the
    top_earlgrey module, but not the padring and ast modules.
    
    Further, the area report is extended to also include logic and macro
    percentages for each module.
    
    Signed-off-by: Michael Schaffner <msf@google.com>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
