#!/bin/bash

file_path=$1

awk '{
    for (i=2; i<=NF; i++) {
        if ($i ~ /[0-9]/) {
            print
            break
        }
    }
}' "$file_path"
