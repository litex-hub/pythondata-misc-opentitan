import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14827"
version_tuple = (0, 0, 14827)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14827")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14685"
data_version_tuple = (0, 0, 14685)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14685")
except ImportError:
    pass
data_git_hash = "1a8644ee02896ec8c8ba8642ae56748f1836dd20"
data_git_describe = "v0.0-14685-g1a8644ee02"
data_git_msg = """\
commit 1a8644ee02896ec8c8ba8642ae56748f1836dd20
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Oct 18 17:47:17 2022 -0700

    [top/dv] Invalidate cache prior to execution from sram
    
    - The test fails from time to time because the first
      execute_from_sram call can be cached.  That means when
      the second call is invoked, it is fetched out of icache
      instead of sram, causing the test to pass.
    
    - The fix is simply to add an invalidate_icache command
      prior to invoking execute from sram.
    
    - This will be something to be aware of when execute from
      sram is used in the future, we should probably always invalidate
      prior to jumping.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
