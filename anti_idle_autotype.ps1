# Stay awake / anti idle script
# Send the specified key (dot) every x seconds


# For how long this script will be executed (in minutes)
param($minutes = 120)

$myshell = New-Object -com "Wscript.Shell"

for ($i = 0; $i -lt $minutes; $i++) {
  Start-Sleep -Seconds 10
  $myshell.sendkeys(".")
}