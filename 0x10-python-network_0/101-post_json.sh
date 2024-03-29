#!/bin/bash
# A script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -s -L -X POST -H 'Content-Type: application/json' -d "$(if [ -f "$2" ]; then cat "$2"; fi)" "$1"
