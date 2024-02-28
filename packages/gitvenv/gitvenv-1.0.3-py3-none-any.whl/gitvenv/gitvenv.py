import os
import shutil
import getpass
import importlib.resources

class GitVEnvError(Exception):
    pass

def _get_gitconfig() -> str | None:
    gitconfig = os.getenv("GIT_CONFIG_GLOBAL")
    if gitconfig is not None:
        return gitconfig

    home = os.path.expanduser("~")

    gitconfig = os.path.join(home, ".gitconfig")
    if os.path.isfile(gitconfig):
        return gitconfig

    config_home = os.getenv("XDG_CONFIG_HOME")
    if config_home is None:
        config_home = os.path.join(home, ".config")

    gitconfig = os.path.join(config_home, "git/config")
    if os.path.isfile(gitconfig):
        return gitconfig

    return None

def _get_ssh_config() -> str | None:
    ssh_config = os.getenv("GIT_VIRTUAL_ENV_SSH_CONFIG")
    if ssh_config is not None:
        return ssh_config

    # openssh doesn't rely on $HOME to get config
    user = getpass.getuser()
    home = os.path.expanduser("~" + user)

    ssh_config = os.path.join(home, ".ssh/config")
    if os.path.isfile(ssh_config) is not None:
        return ssh_config

    return None

def _create_config(src: str | None, dst: str) -> None:
    if src is None:
        with open(dst, "wb"):
            return

    shutil.copy(src, dst)

def create(path: str, clear: bool = False, copy_current: bool = False) -> None:
    if clear:
        try:
            for entry in os.scandir(path):
                if entry.is_dir(follow_symlinks=False):
                    shutil.rmtree(entry.path)
                else:
                    os.remove(entry)
        except FileNotFoundError:
            pass

    binpath = os.path.join(path, "bin")
    os.makedirs(binpath, exist_ok=True)

    with importlib.resources.path(__package__, "scripts") as scripts_path:
        for script in os.scandir(scripts_path):
            srcpath = script.path
            dstpath = os.path.join(binpath, script.name)
            shutil.copyfile(srcpath, dstpath)

    gitconfig = os.path.join(path, "gitconfig")
    ssh_config = os.path.join(path, "ssh_config")

    if not os.path.exists(gitconfig):
        src = None
        if copy_current:
            src = _get_gitconfig()

        _create_config(src, gitconfig)

    if not os.path.exists(ssh_config):
        src = None
        if copy_current:
            src = _get_ssh_config()

        _create_config(src, ssh_config)
