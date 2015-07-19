FROM centos:5

RUN rpm -ivh https://yum.puppetlabs.com/puppetlabs-release-el-5.noarch.rpm; \
  yum install -y puppet; \
  sed -i '$a \\nserver = puppetmaster' /etc/puppet/puppet.conf
