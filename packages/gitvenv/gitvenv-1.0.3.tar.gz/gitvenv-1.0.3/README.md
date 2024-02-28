# gitvenv

Tool to manage multiple Git environments.

Strongly based on python's venv module.

gitvenv defines four environment variables to make the environment work:
 - `GIT_VIRTUAL_ENV` – a convenience variable pointing to the environment directory.
 - `GIT_CONFIG_GLOBAL` – tells Git to use config from the environment.
 - `GIT_VIRTUAL_ENV_SSH_CONFIG` – a convenience variable pointing to SSH config.
 - `GIT_SSH_COMMAND` – tells Git to use SSH command with config from the environment: `$GIT_SSH -F /path/to/env/ssh_config`. If `GIT_SSH` is undefined, `ssh` will be used instead.

## Installation

### Using pip

```bash
pip install gitvenv
```

### Using AUR

```bash
git clone https://aur.archlinux.org/python-gitvenv.git
cd python-gitvenv/
makepkg -si
```

### Using Git

```bash
git clone https://gitlab.com/yataro/gitvenv.git
cd gitvenv/
pip install .
```


## Usage
```
usage: gitvenv [-h] [--clear] [--copy] ENV_DIR

Creates a virtual Git environment in the target directory.

positional arguments:
  ENV_DIR     A directory to create the environment in.

options:
  -h, --help  show this help message and exit
  --clear     Delete the contents of the environment directory if it already exists, before environment creation.
  --copy      Copy the current config files to the new environment.

Once an environment has been created, you may wish to activate it, e.g. by sourcing an activate script in its bin directory.
```

bash and PowerShell are currently supported:

#### bash

```bash
gitvenv my_env/
source my_env/bin/activate

# Use environment
git config --global user.name 'John Doe'
git config --global user.email 'john@example.com'

# Deactivate environment
gitvenv_deactivate
```

#### PowerShell

```powershell
gitvenv my_env/
.\my_env\bin\Activate.ps1

# Use environment
git config --global user.name 'John Doe'
git config --global user.email 'john@example.com'

# Deactivate environment
gitvenv_deactivate
```
