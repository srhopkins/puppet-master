FROM centos:6

RUN rpm -ivh https://yum.puppetlabs.com/puppetlabs-release-el-6.noarch.rpm; \
  yum install -y puppet; \
  sed -i '$a \\nserver = puppetmaster' /etc/puppet/puppet.conf
