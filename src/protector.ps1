if (-NOT ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Break
}

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
Set-MpPreference -DisableRealtimeMonitoring $true