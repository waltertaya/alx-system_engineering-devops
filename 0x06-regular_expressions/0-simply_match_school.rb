#!/usr/bin/env ruby

=begin
   Regular expression must match School.
   Ruby script that accepts one argument and passes it to a regular expression matching method.
=end

puts ARGV[0].scan(/School/).join
