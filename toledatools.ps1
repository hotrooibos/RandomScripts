$curDate = (Get-Date).ToString('yyyyMMdd_HHmm')
$d2BackupURL = "D:\Backups\D2R\" + $curDate + "_d2r_savesbackup.7z"

# Restart Click Monitor DDC
taskkill /F /IM ClickMonitorDDC_7_2.exe
C:\Users\tlda\Apps\ClickMonitorDDC\ClickMonitorDDC_7_2.exe

# Diablo2 local save backup
C:\"Program Files"\7-Zip\7z.exe a -t7z $d2BackupURL C:\Users\tlda\"Saved Games"\"Diablo II Resurrected"\* -r


#
# WINDOWS REINSTALL
#
Start-Sleep -s 10