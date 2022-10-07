pytest -s -v -m "sanity" -n 3 .\testcase\ --browser chrome
REM pytest -s -v -m "regression" -n 3 .\testcase\ --browser chrome
REM pytest -s -v -m "sanity and regression" -n 3 .\testcase\ --browser chrome
REM pytest -s -v -m "sanity or regression" -n 3 .\testcase\ --browser chrome

pytest -s -v -m "sanity" -n 3 .\testcase\ --browser firefox
REM pytest -s -v -m "regression" -n 3 .\testcase\ --browser firefox
REM pytest -s -v -m "sanity and regression" -n 3 .\testcase\ --browser firefox
REM pytest -s -v -m "sanity or regression" -n 3 .\testcase\ --browser firefox

pytest -s -v -m "sanity" -n 3 .\testcase\ --browser edge
REM pytest -s -v -m "regression" -n 3 .\testcase\ --browser edge
REM pytest -s -v -m "sanity and regression" -n 3 .\testcase\ --browser edge
REM pytest -s -v -m "sanity or regression" -n 3 .\testcase\ --browser edge