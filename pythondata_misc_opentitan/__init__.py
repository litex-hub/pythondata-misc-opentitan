import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5398"
version_tuple = (0, 0, 5398)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5398")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5303"
data_version_tuple = (0, 0, 5303)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5303")
except ImportError:
    pass
data_git_hash = "9d9d86fb65b5e5cb16df6cdba89cffe1327ec056"
data_git_describe = "v0.0-5303-g9d9d86fb6"
data_git_msg = """\
commit 9d9d86fb65b5e5cb16df6cdba89cffe1327ec056
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Tue Mar 2 00:15:51 2021 -0800

    [dvsim] Implement LsfLauncher
    
    This is a first cut implementation of the LsfLauncher. There are several
    items left as TODOs - they will be addressed later.
    
    This implementation dispatches all targets (builds, runs, cov etc) as
    job arrays by default. Builds are run discretely (array of 1 job) since
    we consider each build to have specific job requirements that cannot be
    shared with other builds (cpu/mem/disk/stack usage settings - these will
    be added in future). Runs pertaining to a build is dispatched as an
    array. The associated changes made to other sources support the array
    generation.
    
    The job polling is not done by invoking bjobs or bhist, but by looking
    for the LSF job output file (unique for each array index), which gets
    written to only AFTER the job is complete. This offers a really fast way
    to test for completion rather than invoking bjobs or bhist, which bring
    the system to a crawl when invoked for 20k tests in flight. This largely
    works for now, but we need to explore other options such as using IBM's
    Platform LSF Python APIs (future work!).
    
    What launcher system to pick is decided by `DVSIM_LAUNCHER` variable.
    In addition, this PR also adds support for Python virtualenv to isolate
    project-specific python requirements that need to be met when running
    tasks on remote machines used by several other projects as well.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
