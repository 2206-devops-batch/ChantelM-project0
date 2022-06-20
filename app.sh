#! /bin/bash

setup_env(){
    python3 -m venv d_bot
    source d_bot/bin/activate
    pip3 install -r requirements.txt
}

# run tests
run_tests(){
    failed=""
    for i in $(find . -name 'test_*.py'); do
        `python3 $i`

        failed=`grep 'FAILED' test_results.txt`
    done
    echo $failed
}

test_res=$(run_tests)

if [ -z "$test_res" ]; then
    # start server in the background and client in the foreground
    python3 ./src/server/srvrsock.py & python3 ./src/client/game_bot.py && fg
    echo "Press ctrl+c (once) to terminate game_bot.py and sudo fuser -k [PORT]/tcp to terminate the server"
else
    echo "There was a failure. Review test_results.txt"
fi
