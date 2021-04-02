import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5674"
version_tuple = (0, 0, 5674)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5674")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5579"
data_version_tuple = (0, 0, 5579)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5579")
except ImportError:
    pass
data_git_hash = "62dabf7c512b09d6e185df52752d82393338c0b0"
data_git_describe = "v0.0-5579-g62dabf7c5"
data_git_msg = """\
commit 62dabf7c512b09d6e185df52752d82393338c0b0
Author: Timothy Chen <timothytim@google.com>
Date:   Wed Mar 24 12:09:27 2021 -0700

    [reggen, util] Add support for data integrity passthrough
    
    - When a module has no window or has windows with no integrity passthrough,
      data integrity can be generated at a common location.
    
    - When a module window has data integrity passthrough, the regfile
      registers must separately generate data integrity so as to not
      duplicate.
    
    - When a module has a mix of windows with and without integrity, common
      generation is not possible, and data integrity is selectively generated
      for those windows that do not directly pass them in.
    
    - The only module that is currently impacted is otbn (and soon rom_ctrl)
      Otbn dmem / imem each contain their own integrity, and thus can directly
      pass them through.  The regfile for otbn thus no longer generates data
      integrity at a common location, and instead generates it only for data
      passed through tlul_adapter_reg.  The data integrity for the windows are
      fed through directly.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [top] Auto generate files
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
