#!/usr/bin/env ruby

# Coomand line arguments
input_string = ARGV[0] || "Neha loves School, that is why she is a School mentor :)"

# Define the pattern of the regular expression
pattern = /School/

# Check if the input string matches the pattern
match = input_string.match(pattern)

## Print the result
puts match ? match[0] : ''
