import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13211"
version_tuple = (0, 0, 13211)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13211")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13069"
data_version_tuple = (0, 0, 13069)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13069")
except ImportError:
    pass
data_git_hash = "737e1a4407f5a1f2de4da2311bcab48c7b686a9e"
data_git_describe = "v0.0-13069-g737e1a4407"
data_git_msg = """\
commit 737e1a4407f5a1f2de4da2311bcab48c7b686a9e
Author: Muqing Liu <muqing.liu@wdc.com>
Date:   Wed Jul 20 16:56:30 2022 -0700

    [entropy_src, dv] Add covergroup sample functions for entropy_src forced errors
    
      - Add covergroup sample functions in the err_vseq for the forced errors that can't be accessed in the scoreboard
      - Update alert_vseq to accommodate the updates in recov_alert_sts register
      - Fix some path reference bugs in the err_vseq
    
    Signed-off-by: Muqing Liu <muqing.liu@wdc.com>

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
