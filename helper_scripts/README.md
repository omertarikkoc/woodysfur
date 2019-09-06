# Helper Scripts

## remove_sizes.sh
For given sizes removes the duplicate thumbnails images in `site/static/img/uploads` folder.

`echo rm $imageWithSize `
to:

`echo rm $imageWithSize >> result.txt`
which will log everything to the file result.txt and allow you to browse it before really removing them. If all is well change that line to:

`rm $imageWithSize`

If you're curious here is what the regex does:
[a-z-]* looks for filenames like foo-bar or fo-fo-bar. if you have uppercase letters in your name use [A-Za-z-]*
-[0-9] after the filename it looks for the remaining - (dash) with a number [0-9]
.*.txt looks for anything after the first digit to the end of the name with the extension.
After completing the scripting and running it. You could blow everything away on your site and re-upload the images. If you're worried about file size I would even use imagemagick but I prefer sips to reduce the compression size of the images.

