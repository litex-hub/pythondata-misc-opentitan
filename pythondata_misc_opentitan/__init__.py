import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11427"
version_tuple = (0, 0, 11427)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11427")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11301"
data_version_tuple = (0, 0, 11301)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11301")
except ImportError:
    pass
data_git_hash = "88109a0f8955bab1949fc4e000a7488802ace242"
data_git_describe = "v0.0-11301-g88109a0f8"
data_git_msg = """\
commit 88109a0f8955bab1949fc4e000a7488802ace242
Author: Cindy Liu <hcindyl@google.com>
Date:   Wed Mar 30 19:19:24 2022 -0700

    [ipgen, rv_plic] Enable specific module_instance_name for multiple plic groups
    
    Current ipgen for rv_plic only allow a single rv_plic group, and
    generate the `ip_autogen` based on the template name. Adding a field in
    the parameter `module_instance_name` to allow more plic groups to be
    generated.
    
    To support this, all the non-template files in `hw/ip_templates/rv_plic`
    (except docs) are converted to mako template files.
    
    It is a no-op for top_earlgrey, with the slight EOF newline change from
    the generated files.
    
    Signed-off-by: Cindy Liu <hcindyl@google.com>

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
