import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14678"
version_tuple = (0, 0, 14678)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14678")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14536"
data_version_tuple = (0, 0, 14536)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14536")
except ImportError:
    pass
data_git_hash = "f0d65e65aeefdc0ca79097acf7c79e1fd683ac92"
data_git_describe = "v0.0-14536-gf0d65e65ae"
data_git_msg = """\
commit f0d65e65aeefdc0ca79097acf7c79e1fd683ac92
Author: Andreas Kurth <adk@lowrisc.org>
Date:   Fri Sep 30 17:24:32 2022 +0000

    [top/dv] Add test glitching outputs of Ibex or lockstep core
    
    This commit contributes to resolving lowRISC/ibex#1757.  A subsequent
    commit shall extend this test to also glitch the inputs of the lockstep
    core.
    
    Signed-off-by: Andreas Kurth <adk@lowrisc.org>

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
