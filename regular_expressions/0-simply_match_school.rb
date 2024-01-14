#!/usr/bin/env ruby

# Coomand line arguments
input_string = ARGV[0]

# Define the pattern of the regular expression
pattern = /School/

# Check if the input string matches the pattern
match = input_string.match(pattern)

## Print the result
puts match ? match[0] : ''
