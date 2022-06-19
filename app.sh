#! /bin/bash

serverScript='./src/server/srvrsock.py'
botScript='./src/client/game_bot.py'

# run tests
run_tests(){
    failed=""
    for i in $(find . -name 'test_*.py'); do
        `python3 $i`

        failed=`grep 'FAILED' test_results.txt`
    done
    echo $failed
}

# start server
start_server(){
    python3 ./src/server/srvrsock.py &
    echo $$
}

# start bot
start_bot(){
    python3 ./src/client/game_bot.py &
    echo $$
}

test_res=$(run_tests)

if [ -z "$test_res" ]; then
    # serverPID=$(start_server)
    # botPID=$(start_bot)
    python3 ./src/server/srvrsock.py & python3 ./src/client/game_bot.py && fg
else
    echo "There was a failure. Review test_results.txt"
fi
