# !/bin/bash

USERNAME=tarik
DIRECTORY="/Users/$USERNAME/prj/woodysfur/site/static/img/uploads"
echo "Hello world"
for imageWithSize in $(find "$DIRECTORY" -type f -regex '.*/[a-z-]*-[0-9].*.jpeg$'); do
    cd $DIRECTORY
    echo rm $imageWithSize
done