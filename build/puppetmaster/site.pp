node puppetmaster {
  # Configure puppetdb and its underlying database
  class { 'puppetdb': }
  # Configure the puppet master to use puppetdb
  class { 'puppetdb::master::config': }
}
