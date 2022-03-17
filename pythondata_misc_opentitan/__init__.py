import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10935"
version_tuple = (0, 0, 10935)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10935")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10809"
data_version_tuple = (0, 0, 10809)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10809")
except ImportError:
    pass
data_git_hash = "30d626cc8a5ccdf74b13ca57e87291fd0ead9aed"
data_git_describe = "v0.0-10809-g30d626cc8"
data_git_msg = """\
commit 30d626cc8a5ccdf74b13ca57e87291fd0ead9aed
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Wed Mar 16 19:00:34 2022 -0700

    [chip dv] Testplan mapping fixes
    
    Fix incorrect test mapping that result in unmapped tests in the report.
    Remove _test suffix in tests specified in the hjson, since it is not
    needed.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
