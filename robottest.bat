@echo off
SET /P tags=Please enter tags (or none if no tags) 

set sikulix_jar=C:<location>\sikulixapi.jar
set robot_framework_jar=C:<location>\robotframework-3.0.2.jar

Set FileName=results\%date:~0,2%\%time:~0,2%-%time:~3,2%-%time:~6,2%\
echo %FileName%

if "%tags%"=="none"  (
	java -cp "%robot_framework_jar%;%sikulix_jar%" ^
     -Dpython.path="%sikulix_jar%/Lib" ^
     org.robotframework.RobotFramework ^
     --pythonpath=calc.sikuli:testRedFin.sikuli ^
     --outputdir=r%FileName%^
     --loglevel=TRACE ^
     %*
     ) else (
     java -cp "%robot_framework_jar%;%sikulix_jar%" ^
     -Dpython.path="%sikulix_jar%/Lib" ^
     org.robotframework.RobotFramework ^
     --pythonpath=calc.sikuli:testRedFin.sikuli ^
     --outputdir=%fileName% ^
     --loglevel=TRACE ^
     --include=%tags% ^
     %*
     )