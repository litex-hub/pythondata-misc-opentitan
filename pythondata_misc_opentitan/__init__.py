import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9366"
version_tuple = (0, 0, 9366)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9366")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9249"
data_version_tuple = (0, 0, 9249)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9249")
except ImportError:
    pass
data_git_hash = "30fced74b749946898a6c655e9f81895e8d8400d"
data_git_describe = "v0.0-9249-g30fced74b"
data_git_msg = """\
commit 30fced74b749946898a6c655e9f81895e8d8400d
Author: Weicai Yang <weicai@google.com>
Date:   Wed Jan 5 22:19:04 2022 -0800

    [sram/dv] Update testplan and fix unmapped test
    
    Remove partiy test as it's replaced by passthru_mem_tl_intg_err
    Add stress_all
    
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
