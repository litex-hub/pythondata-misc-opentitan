import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10801"
version_tuple = (0, 0, 10801)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10801")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10675"
data_version_tuple = (0, 0, 10675)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10675")
except ImportError:
    pass
data_git_hash = "3dcc25e60d768d679103bbf381e0204d988f2e54"
data_git_describe = "v0.0-10675-g3dcc25e60"
data_git_msg = """\
commit 3dcc25e60d768d679103bbf381e0204d988f2e54
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Wed Mar 9 09:28:27 2022 +0000

    Update lowrisc_ibex to lowRISC/ibex@3438b779
    
    Update code from upstream repository
    https://github.com/lowRISC/ibex.git to revision
    3438b77921941ccbf50cba46b3009a6a37203d4b
    
    * [rtl] Add minor alert for icache ECC error (Greg Chadwick)
    * [icache, rtl] Fix ECC error indication (Greg Chadwick)
    * [rtl] Add SEC_CM markers for security features (Greg Chadwick)
    * [ibex, dv] Makes delays between req, gnt and rvalid configurable
      (Prajwala Puttappa)
    * [ibex, dv] Added new base, interrupt, debug and mem error sequences
      (Prajwala Puttappa)
    * [icache] Define some fake DPI functions to simplify linking (Rupert
      Swarbrick)
    * [ibex, dv] Added agent configuration for
      ibex_mem_intf_response_agent (Prajwala Puttappa)
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

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
