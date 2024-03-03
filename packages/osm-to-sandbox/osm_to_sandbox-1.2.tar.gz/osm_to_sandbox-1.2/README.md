# OpenStreetMap To Sandbox

This is a script to download data from OSM API and upload it to the
[mapping sandbox](https://wiki.openstreetmap.org/wiki/Sandbox_for_editing).

Note that it clears all data in the sandbox beforehand. NEVER change
endpoint addresses in the script.

## Installation

    pip install --user osm-to-sandbox

## Usage

Open the [bounding box tool](https://boundingbox.klokantech.com/),
draw a box, choose "CSV" format below, and copy the numbers. Then do:

    osm_to_sandbox 1.2,3.4,5.6,7.8 --auth

Where numbers are your bbox. The `--auth` flag is required and will prompt for the Sandbox username and password. [Get these here](https://master.apis.dev.openstreetmap.org/user/new). The script would download the data from both
servers, then it would start doing its uploading work.

## Author

Written by Ilya Zverev, published under ISC license.
