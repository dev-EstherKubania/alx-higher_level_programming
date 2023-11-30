#!/bin/bash
# Display accepted HTTP methods for a URL using curl
curl -sI -X OPTIONS "$1" | grep "Allow" | cut -d ' ' -f 2-
