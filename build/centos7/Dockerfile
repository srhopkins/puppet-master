FROM centos:7

RUN rpm -ivh https://yum.puppetlabs.com/puppetlabs-release-el-7.noarch.rpm; \
  yum install -y puppet; \
  sed -i '$a \\nserver = puppetmaster' /etc/puppet/puppet.conf
