import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14673"
version_tuple = (0, 0, 14673)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14673")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14531"
data_version_tuple = (0, 0, 14531)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14531")
except ImportError:
    pass
data_git_hash = "08334590b8b26212fc4525f4b5cb14d3ec5fdec3"
data_git_describe = "v0.0-14531-g08334590b8"
data_git_msg = """\
commit 08334590b8b26212fc4525f4b5cb14d3ec5fdec3
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Mon Oct 10 09:56:47 2022 -0700

    [entropy_src/dv] Refactor scoreboarding collect_entropy
    
    When scoreboarding results from the ExtHT agent the scoreboard needs to
    wait for the ExtHT agent to report back.  Since the agent is slightly
    delayed by the DUT, this means that the health test scoring must also
    be delayed.
    
    This commit breaks entropy collection and health test scoring into
    separate threads so that the health test scoring can be done at the
    appropriate time.
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

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
