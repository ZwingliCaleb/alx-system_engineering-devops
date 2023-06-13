#This puppet file fixes the too many open files error

exec { 'Fix hard limit':
  command => '/usr/bin/env sed -i "s/4/20000/; s/5/20000/" /etc/security/limits.conf'
}
