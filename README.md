# inkscape-eps-export

AI compatible EPS export for Inkscape 0.92 (might work with older versions too)

This script converts an Inkscape SVG to Adobe Illustrator 7 compatible EPS.
The generated EPS file uses custom Illustrator PS operators, and includes
PostScript processes that stands in place of said operators when the file is
not opened with Adobe Illustrator.

The script exports layers, groups, paths, clones, clipping paths, fill, stroke,
gradient fill into a format that Illustrator understands.

**Warning**
This script is not extensively tested. Since its dual nature, it is possible
that the result looks different in Illustrator than in other programs.

## Installation
Copy aieps_output.inx and aieps_output.py  into the Inkscape extensions folder:

* On Windows C:\\Program Files\\Inkscape\\share\\extensions
* On Linux /usr/share/inkscape/extensions

## Known limitations

* Text is not supported: convert them to paths, then ungroup them.  
  You can regroup them afterwards, but without ungrouping, this script may think
  they are invisible.
* Path node types are not retained.
* Circles and elliptical arc segments in paths are converted to bezier curves.
* Layer names lose non 7 bit ASCII characters.
* Radial gradients cannot be elliptical: all radial gradients will be converted
  to circular. (Although I think it is possible to save elliptical radial
  gradients, but I did not figure out how to save it in a way that is compatible
  with different Illustrator versions.)
* Outline gradients are not supported. (Illustrator 7 does not support them.)
* Clones are exported as copies.
* No transparency: everything is exported opaque. (EPS does not support transparency.)
* Filters (including radial blur) are not exported.
* Path effects are not exported, only the result of the effects.

## Features
(It’s not a bug, it’s a feature!)

* Automatically closes all paths that are filled. It makes visual difference
  with unclosed paths that have fill and stroke.
* Invisible objects are not exported (invisible layers and objects, objects
  with neither stroke nor fill, stray points)
