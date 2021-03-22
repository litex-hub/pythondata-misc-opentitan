import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5505"
version_tuple = (0, 0, 5505)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5505")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5410"
data_version_tuple = (0, 0, 5410)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5410")
except ImportError:
    pass
data_git_hash = "a4a7e84dec68e8e938d1a28c37468c799d40be78"
data_git_describe = "v0.0-5410-ga4a7e84de"
data_git_msg = """\
commit a4a7e84dec68e8e938d1a28c37468c799d40be78
Author: Udi Jonnalagadda <udij@google.com>
Date:   Wed Mar 17 18:01:58 2021 -0700

    [dv/regr] update result paths for sram/kmac
    
    this PR updates the result paths for both the KMAC and SRAM IPs, as both
    have two variants that are tested.
    
    currently, the regression results are published to:
    `reports.opentitan.org/hw/ip/kmac/dv/latest/results.html`,
    where the segment of `hw/ip/kmac/dv` is set to a variable called
    `{rel_path}` inside of `common_project_cfg.hjson`.
    
    having both variants write regression results to the same link
    will result in something breaking, so this `rel_path` variable is now
    overridden in the `base_sim_cfg.hjson` for both IPs so that the variant
    name is now factored into the results link to "uniquify" things.
    
    Signed-off-by: Udi Jonnalagadda <udij@google.com>

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
