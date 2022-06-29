import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12876"
version_tuple = (0, 0, 12876)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12876")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12734"
data_version_tuple = (0, 0, 12734)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12734")
except ImportError:
    pass
data_git_hash = "67ba900f5e83c07dff0aa3c4acd95005b04d7bea"
data_git_describe = "v0.0-12734-g67ba900f5e"
data_git_msg = """\
commit 67ba900f5e83c07dff0aa3c4acd95005b04d7bea
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Sat Jun 4 10:11:42 2022 -0700

    [entropy_src/dv] Test support for SW_REGUPD and CSR autolock
    
    - entropy_src_rng_vseq now randomly reconfigures the DUT while it is
      enabled or while SW_REGUPD is zero.  Such events should have no
      impact on the DUT in these states.
      - Adds a new timing parameter, mean_rand_reconfig_time
        to control the average frequency of these random events.
        Like the hard_mtbf, and soft_mtbf parameters, these
        events occur with an exponential distribution, meaning
        that on average the probability of such an update occuring
        in a period of duration dt is:
        P(t)dt = dt/mean_rand_reconfig_time
      - These update events are also scheduled to NOT happen
        during other maintaince events (DUT resets, FIFO reads,
        etc).
    - Updates the Scoreboard to properly support this feature
    - Adds support in the rng and base vseqs for generating new
      configurations, subject to the same original constraints.
    - In order to support the randomization of DUT configurations
      a new entropy_src_dut_cfg class is added to separate the
      config fields that describe DUT configs from more generic
      environment or sequence configurations.
    
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
