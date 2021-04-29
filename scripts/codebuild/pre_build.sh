echo "[Pre-Build phase - run unit tests] `date` in `pwd`"

python run_all_tests.py ||  { echo 'Auto Tests Failed' ; exit 1; }