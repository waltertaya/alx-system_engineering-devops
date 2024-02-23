# Puppet manifest to install Flask version 2.1.0 using pip3

# Install Flask package
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
