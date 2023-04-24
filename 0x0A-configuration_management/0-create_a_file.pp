# create a file in /tmp using puppet


file {'/tmp/school':
content => 'I Love Puppet',
owner => 'www-data',
group => 'www-data',
mode => '0744'}
