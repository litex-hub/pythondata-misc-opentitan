import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5608"
version_tuple = (0, 0, 5608)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5608")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5513"
data_version_tuple = (0, 0, 5513)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5513")
except ImportError:
    pass
data_git_hash = "c7a5044e87da31cf4b4d8bb62a9c0f7ac639bdab"
data_git_describe = "v0.0-5513-gc7a5044e8"
data_git_msg = """\
commit c7a5044e87da31cf4b4d8bb62a9c0f7ac639bdab
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Thu Mar 25 21:47:56 2021 -0700

    [dvsim] Keep dependencies list
    
    This set of changes is aimed at retaining the dependency order across
    targets, even if the dependency is not scheduled to be run. The
    Deploy::dependencies list once constructed, remains untouched. We
    instead change the way the FlowCfg::deploy list is created - if targets
    are not required to run (for example, when --build-only or --run-only
    switch is passed), then they are not added to the deploy list. This
    means that the deploy list needs to be constructed correctly - the
    scheduler relies on it to know what to run.
    
    The scheduler previously recursively went through the dependencies to
    determine what all needed to be run - this required the FlowCfg to
    delete dependencies after the fact, if flow modifier switches were
    passed. This is no longer needed because we now explicitly provide it
    the list of things to run instead. This also means when checking an
    item's eligibility to be enqueued based on its dependencies' statuses,
    it needs to ignore the deps that were not a part of the original deploy
    list.
    
    The reason for this change is our internal Google Cloud based launching
    system, which runs each job (input -> process -> output) in an isolated
    VM instance. The job's input and output are tarballs that flit between
    the user's workstation, Google Cloud storage, and the VM instance. To
    support --run-only for example, in our environment, the run deploy
    object needs to be able to provide a pointer to its build dependency
    (which would have run in the past) so that the built simulation
    executable can be tarballed and uploaded as the run-job's input.
    
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
