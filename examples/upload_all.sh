#!/bin/sh

#
# This script uploads all the files to the device
#

if ! command -v mpremote >/dev/null 2>&1; then
    echo "This script requires the mpremote command. You can install it with:"
    echo "pip3 install --user mpremote"
    exit 1
fi

if ! command -v mpy-cross >/dev/null 2>&1; then
    echo "This script requires the mpy-cross command. You can install it with:"
    echo "pip3 install --user mpy-cross"
    exit 1
fi

upload_fonts () {
    cd ../romfonts
    rm -f *.mpy
    for font in *.py
    do
        compile $font
    done
    cd ..
    mpremote cp romfonts/*.mpy :
    cd examples
}

upload () {
    echo "Uploading $1"
    mpremote cp $1 :
}

compile () {
    echo "Compiling $1"
    mpy-cross $1
}

compile_upload () {
    source="$1"
    compiled="${source%.py}.mpy"
    compile ${source}
    upload ${compiled}
}

select_menu() {
    local subdirectories=()
    directory="$2"
    selection=""

    # Display the title
    echo -e "\n$1\n"

    # Populate the subdirectories array
    while IFS= read -r subdirectory; do
        subdirectories+=("$subdirectory")
    done < <(find "$directory" -mindepth 1 -type d -printf "%f\n")

    # Display the menu
    PS3="Select a subdirectory (enter 0 to cancel): "
    select subdirectory in "${subdirectories[@]}"; do
        if [[ "$REPLY" == "0" ]]; then
            echo "Canceled."
            exit 1
        elif [[ -n "$subdirectory" ]]; then
            selection="$subdirectory"
            break
        else
            echo "Invalid selection. Please try again."
        fi
    done

    echo "Selected subdirectory: ${directory}/${selection}"
}

select_menu "Select a configuration to upload:" "../tft_configs"
upload "${directory}/${selection}/*.py"

# Driver
upload "../lib/st7789py.py"

# Fonts
upload_fonts

compile_upload alien/alien_bitmap.py
upload alien/alien.py

upload feathers.py
upload rotations.py
upload scroll.py
upload fonts.py
upload hello.py
upload color_test.py

upload tiny_toasters/tiny_toasters.py
compile_upload tiny_toasters/tiny_toasters_bitmaps.py

upload boxlines.py

upload proverbs/proverbs.py
compile_upload proverbs/proverbs_20.py
compile_upload proverbs/proverbs_30.py

upload roids.py

upload chango/chango.py
compile_upload chango/chango_16.py
compile_upload chango/chango_32.py
compile_upload chango/chango_64.py

upload noto_fonts/noto_fonts.py
compile_upload noto_fonts/NotoSans_32.py
compile_upload noto_fonts/NotoSansMono_32.py
compile_upload noto_fonts/NotoSerif_32.py

upload tiny_hello.py
