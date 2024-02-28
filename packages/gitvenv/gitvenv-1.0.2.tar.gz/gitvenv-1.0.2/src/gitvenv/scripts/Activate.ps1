function global:gitvenv_deactivate ([switch]$NonDestructive) {
    if (Test-Path -Path Env:GIT_CONFIG_GLOBAL) {
        Remove-Item -Path Env:GIT_CONFIG_GLOBAL
    }
    if (Test-Path -Path Env:GIT_SSH_COMMAND) {
        Remove-Item -Path Env:GIT_SSH_COMMAND
    }
    if (Test-Path -Path Env:GIT_VIRTUAL_ENV) {
        Remove-Item -Path Env:GIT_VIRTUAL_ENV
    }
    if (Test-Path -Path Env:GIT_VIRTUAL_ENV_SSH_CONFIG) {
        Remove-Item -Path Env:GIT_VIRTUAL_ENV_SSH_CONFIG
    }

    # Restore variables
    if (Test-Path -Path Env:_GIT_VENV_OLD_CONFIG_GLOBAL) {
        Copy-Item -Path Env:_GIT_VENV_OLD_CONFIG_GLOBAL -Destination Env:GIT_CONFIG_GLOBAL
        Remove-Item -Path Env:_GIT_VENV_OLD_CONFIG_GLOBAL
    }
    if (Test-Path -Path Env:_GIT_VENV_OLD_SSH_COMMAND) {
        Copy-Item -Path Env:_GIT_VENV_OLD_SSH_COMMAND -Destination Env:GIT_SSH_COMMAND
        Remove-Item -Path Env:_GIT_VENV_OLD_SSH_COMMAND
    }

    if (-not $NonDestructive) {
        Remove-Item -Path Function:gitvenv_deactivate
    }
}

gitvenv_deactivate -NonDestructive

$GitVirtualEnv = (Get-Item -Path $MyInvocation.MyCommand.Definition).Directory.Parent
$Env:GIT_VIRTUAL_ENV = $GitVirtualEnv

# Backup variables
if (Test-Path -Path Env:GIT_CONFIG_GLOBAL) {
    Copy-Item -Path Env:GIT_CONFIG_GLOBAL -Destination Env:_GIT_VENV_OLD_CONFIG_GLOBAL
}
if (Test-Path -Path Env:GIT_SSH_COMMAND) {
    Copy-Item -Path Env:GIT_SSH_COMMAND -Destination Env:_GIT_VENV_OLD_SSH_COMMAND
}

# Use gitconfig from environment
$Env:GIT_CONFIG_GLOBAL = Join-Path -Path $GitVirtualEnv -ChildPath "gitconfig"

# Use ssh_config from environment
$GitVirtualEnvSshConfig = Join-Path -Path $GitVirtualEnv -ChildPath "ssh_config"
$Env:GIT_VIRTUAL_ENV_SSH_CONFIG = $GitVirtualEnvSshConfig
if (Test-Path -Path Env:GIT_SSH) {
    $GitVirtualEnvSsh = "'$($Env:GIT_SSH.Replace("'", "'\\''"))'"
} else {
    $GitVirtualEnvSsh = "ssh"
}
$Env:GIT_SSH_COMMAND = "$GitVirtualEnvSsh -F '$($GitVirtualEnvSshConfig.Replace("'", "'\\''"))'"
