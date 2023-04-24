# Setting up client-side SSH config for logging in  without a password.

include stdlib

file_line {'Declarative identity file':
  path    => '/etc/ssh/ssh_config',
  line    => '   IdentityFile ~/.ssh/school',
  replace => true
}
file_line {'Turn off passwd auth':
  path    => '/etc/ssh/ssh_config',
  line    => '     PasswordAuthentication no',
  replace => true
}

