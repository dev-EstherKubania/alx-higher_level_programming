#!/bin/bash
# This script sends a POST request with specified variables and displays the response
curl -s -X POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
