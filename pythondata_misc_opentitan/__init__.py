import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8928"
version_tuple = (0, 0, 8928)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8928")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8816"
data_version_tuple = (0, 0, 8816)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8816")
except ImportError:
    pass
data_git_hash = "d9881e47c0acd1195b184d55e010be27e086ab20"
data_git_describe = "v0.0-8816-gd9881e47c"
data_git_msg = """\
commit d9881e47c0acd1195b184d55e010be27e086ab20
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Tue Nov 23 17:30:20 2021 -0800

    [chip, dv] Move OTP image generation to DVSim
    
    There are a few updates in this commit.
    1. The initial OTP image generation was handled by meson build.
    Unfortulately, that prevents us from modifying the OTP image generation
    in the extended closed source env which has a different OTP memory
    layout than our generic model. The OTP generation step for DV is done
    via DVSim (added to chip_sim_cfg.hjson as a `pre_run_cmd`)
    2. All available OTP image flavors (for LC state RAW, DEV and RMA) are
    constructed by default.
    3. The chip_env_cfg now has supprt for choosing which of these flavors
    to pick via a plusarg.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
