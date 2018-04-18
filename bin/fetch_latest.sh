#!/bin/bash
cd "$(dirname "${BASH_SOURCE[0]}")" || exit 1
MYNAME=$(basename "${BASH_SOURCE[0]}")
BIN_DIR=$(pwd)
REPOS="$BIN_DIR/repos"

[[ -d $REPOS ]] || mkdir -v "$REPOS"
cd "$REPOS" || exit 1

if [[ -d uap-python ]]
then
    echo "Pulling down upstream changes"
    cd uap-python || exit 1
    git pull --ff-only || exit 2
    git submodule update || exit 2
else
    echo "Cloning upstream repo"
    git clone https://github.com/ua-parser/uap-python.git uap-python \
         --recurse-submodules || exit 2
    cd uap-python || exit 1
fi

# Confirm that the checkout still contains all the expected folders; If not
# this script will need to be updated to reflect whatever upstream changes.

[[ -d ua_parser ]] || { echo "Upstream git repo missing 'ua_parser'"; exit 3; }
[[ -d uap-core ]] || { echo "Upstream git repo missing 'uap-core'"; exit 3; }

echo "Copying updated python modules into TA-user-agents"
rm -rf "$BIN_DIR/ua_parser" "$BIN_DIR/uap-core"
mkdir "$BIN_DIR/ua_parser" "$BIN_DIR/uap-core"
# Skip all hidden files
cp -a ua_parser/* "$BIN_DIR/ua_parser"
cp -a uap-core/* "$BIN_DIR/uap-core"

cd "$BIN_DIR" || exit 1

# Stage updates to known files (adds and deletes)
git add -u ua_parser uap-core

# Add any newly created files (not previously part of the upstream repo)
git add ua_parser uap-core

UAP_PY_VER=$(git -C "$REPOS/uap-python" describe)
UAP_CORE_VER=$(git -C "$REPOS/uap-python/uap-core" describe)

git commit -m "$MYNAME python module update

uap-python $UAP_PY_VER
uap-core $UAP_CORE_VER" --edit

