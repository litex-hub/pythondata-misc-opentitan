import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10146"
version_tuple = (0, 0, 10146)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10146")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10022"
data_version_tuple = (0, 0, 10022)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10022")
except ImportError:
    pass
data_git_hash = "5dfe96ba8da3c19400ceeebed338e5ab665521f0"
data_git_describe = "v0.0-10022-g5dfe96ba8"
data_git_msg = """\
commit 5dfe96ba8da3c19400ceeebed338e5ab665521f0
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Thu Feb 3 17:12:39 2022 -0800

    [cdc] Working version of CDC waivers
    
    * Waiver should not have spaces between the status braces.
      changed to `-status {Waived}`
    
    * `[info exists ...]` should use variable name not the value of variable
      changed to `[info exists modules]` in `cdc_waivers.tcl`
    
    * waiver directory is used to source individual waiver files.
      defined `CDC_WAIVERS_DIR
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
