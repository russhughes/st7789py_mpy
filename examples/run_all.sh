#!/bin/sh

#
# Runs all the examples for 5 seconds each
#

function runfor() {
    echo "Running for $1 $2"
    local duration=$1
    shift
    local command="$@"

    # Run the command in the background
    mpremote run $command &

    # Get the process ID of the command
    local pid=$!

    # Sleep for the specified duration
    sleep "$duration"

    # Terminate the command process
    kill "$pid" >/dev/null 2>&1

}

runfor 5 alien/alien.py
runfor 5 feathers.py
runfor 5 rotations.py
runfor 5 scroll.py
runfor 5 fonts.py
runfor 5 hello.py
runfor 5 color_test.py
runfor 5 tiny_toasters/tiny_toasters.py
runfor 5 boxlines.py
runfor 5 proverbs/proverbs.py
runfor 5 roids.py
runfor 5 chango/chango.py
runfor 5 noto_fonts/noto_fonts.py
runfor 5 tiny_hello.py
