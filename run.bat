timeout 5
for %%G in (.\STLs\*) do (
	start "C:\Program Files\Ultimaker Cura 5.0.0\Ultimaker-Cura.exe" %%G
	timeout /t 4 /nobreak
	START /W pixel.exe 2300 1300
	timeout /t 1 /nobreak
	nircmd.exe savescreenshot D:\render\%%~nxG.png)