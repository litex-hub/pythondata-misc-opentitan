import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10817"
version_tuple = (0, 0, 10817)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10817")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10691"
data_version_tuple = (0, 0, 10691)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10691")
except ImportError:
    pass
data_git_hash = "1432b8cd9c33815045547a550df5e25c9ea22918"
data_git_describe = "v0.0-10691-g1432b8cd9"
data_git_msg = """\
commit 1432b8cd9c33815045547a550df5e25c9ea22918
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Mon Mar 7 13:43:18 2022 -0800

    [kmac] Make alert status stay
    
    In issue #10760, @cindychip found that the alert status does not keep
    its value as the status register is set to external register. As
    `alert_operation` just asserts one cycle, the STATUS value becomes zero
    at the next cycle.
    
    In this commit, reg is defined to keep the value. It can be reset by
    err_processed (not the alert but the STATUS value) for recoverable
    error but the fatal error remains high until the IP is being reset.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

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
