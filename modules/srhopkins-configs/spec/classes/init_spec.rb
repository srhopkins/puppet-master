require 'spec_helper'
describe 'configs' do

  context 'with defaults for all parameters' do
    it { should contain_class('configs') }
  end
end
