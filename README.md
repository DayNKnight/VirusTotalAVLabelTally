# Virus Total AV Label Tallier

This is just a quick description of what this does until I update the readme further.

## What it does

This script is meant to take in a file that is filled with malware hashes 
that are of the same type and tally all of the various detections that were given to it by AV companies on Virus Total.  

The reason that I wrote this was so that I could give it hashes that I knew were of the same malware family and get a tally of the most used signatures by the AV companies so that I could figure out what would be the best signature to sort by and also what AV detected the sample the most.

Currently, the script does not merge similar versions from the same AV.

To run it, first install the python requirements by doing (Requires python 3.8):
    
    pipenv install



## To be added in later:

- The ability to add arguments to input to the program.
- A tally of the total of how many times the AV was able to detect the sample as malicious.

These will eventually come (hopefully soon), as this was hastily written in 30 min.

Something that may take longer to implement:

- The ability to merge versions for each AV