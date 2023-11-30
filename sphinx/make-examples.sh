#!/bin/sh

EXAMPLES=$(cat << 'EOF'
alien/alien.py
boxlines.py
chango/chango.py
colorbars/colorbars.py
color_test.py
feathers.py
fonts.py
hello.py
noto_fonts/noto_fonts.py
proverbs/proverbs.py
roids.py
rotations.py
scroll.py
tiny_hello.py
tiny_toasters/tiny_toasters.py
EOF
)

UTILITES=$(cat << 'EOF'
create_png_examples.py
image_converter.py
make_colorbars_bitmap.py
sprites_converter.py
text_font_converter.py
write_font_converter.py
EOF
)

function get_docstring() {
    docstring=$(awk '/^ *"""/ { if (++count == 2) exit; p = !p; next } /NOTE:/ { exit } p { print }' "$1")
}


# expects a string, a variable name, and an optional underline character
# $1 = string
# $2 = variable name
# $3 = underline character (optional)

function make_header() {
    if [ -z "$1" ]; then
        echo "Error: No text provided"
        return 1
    fi

    if [[ ! $2 =~ ^[a-zA-Z_][a-zA-Z0-9_]*$ ]]; then
        echo "Error: Invalid variable name"
        return 1
    fi

    if [ ! -z "$3" ] && [ ${#3} -ne 1 ]; then
        echo "Error: Underline character must be a single character"
        return 1
    fi

    local TEXT="$1"
    local LENGTH=${#TEXT}
    local UNDERLINE_CHAR=${3:-"="}
    local UNDERLINE=""
    for ((i=1; i<=LENGTH; i++)); do
        UNDERLINE+="${UNDERLINE_CHAR}"
    done
    local HEADER="${TEXT}\n${UNDERLINE}"
    eval $2="'$HEADER'"
}

function update_examples() {
    rm -f source/examples/*.rst

    for file_name in $EXAMPLES; do
        echo "file_name: ${file_name}"
        EXAMPLE=$(basename "${file_name}")
        RST_FILE="source/examples/${EXAMPLE%.py}.rst"
        get_docstring "../examples/${file_name}"
        {
            echo ".. _${EXAMPLE%.py}:"
            echo ""
            echo "${docstring}"
            echo ""
            echo ".. literalinclude:: ../../../examples/${file_name}"
            echo "   :language: python"
            echo "   :linenos:"
            echo "   :lines: 1-"
            echo ""
        } > "${RST_FILE}"
    done
}

function upate_configs() {
    find ../tft_configs/ -mindepth 1 -type d | while IFS= read -r directory; do
        if [ "${directory}" != "../tft_configs" ]; then
            EXAMPLE=$(basename "${directory}")
            if [ -f "${directory}/tft_config.py" ]; then
                get_docstring "${directory}/tft_config.py"
                RST_FILE="source/configs/${EXAMPLE%.py}.rst"
                TITLE=$(head -n 1 "${directory}/tft_config.py" | cut -b 4-)
                TITLE_LENGTH=${#TITLE}
                MAIN_HEADER=$(printf '=%.0s' $(seq 1 "${TITLE_LENGTH}"))
                make_header "${directory#../}/tft_config.py" "SUB_HEADER" "^"
                {
                    echo ".. _${directory}:"
                    echo ""
                    echo "$TITLE"
                    echo "$MAIN_HEADER"
                    echo ""
                    echo "${docstring}"
                    echo ""
                    echo -e "${SUB_HEADER}"
                    echo ""
                    echo ".. literalinclude:: ../../../tft_configs/${EXAMPLE}/tft_config.py"
                    echo "   :language: python"
                    echo "   :linenos:"
                    echo "   :lines: 1-"
                    echo ""
                } > "${RST_FILE}"
            fi
            if [ -f "${directory}/tft_buttons.py" ]; then
                get_docstring "${directory}/tft_buttons.py"
                RST_FILE="source/configs/${EXAMPLE%.py}.rst"
                make_header "${directory#../}/tft_buttons.py" "NAME" "^"
                {
                    echo ""
                    echo -e "${NAME}"
                    echo ""
                    echo "${docstring}"
                    echo ""
                    echo ".. literalinclude:: ../../../tft_configs/${EXAMPLE}/tft_buttons.py"
                    echo "   :language: python"
                    echo "   :linenos:"
                    echo "   :lines: 1-"
                    echo ""
                } >> "${RST_FILE}"
            fi
        fi
    done
}

function update_utilites() {
    rm -f source/utilities/*.rst

    for file_name in $UTILITES; do
        echo "file_name: ${file_name}"
        EXAMPLE=$(basename "${file_name}")
        RST_FILE="source/utilities/${EXAMPLE%.py}.rst"
        get_docstring "../utils/${file_name}"
        make_header "${EXAMPLE}" "NAME" "-"
        {
            echo ".. _${EXAMPLE%.py}:"
            echo ""
            echo -e "${NAME}"
            echo "${docstring}"
            echo ""
        } > "${RST_FILE}"
    done
}

function hack_index() {
    {
        echo "Index"
        echo "#####"
        echo ""
    } > source/genindex.rst
}

update_examples
upate_configs
update_utilites
hack_index
