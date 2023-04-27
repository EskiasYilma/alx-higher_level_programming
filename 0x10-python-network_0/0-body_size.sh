#!/bin/bash
response=$(curl -s "$1" | wc -c)
echo "$response"
