# A sample Guardfile
# More info at https://github.com/guard/guard#readme
#
# Installation requirements:
#
#   gem install guard-livereload
#
# Browser plugins:
#   All: http://help.livereload.com/kb/general-use/browser-extensions
#   Firefox (2.0.9 dev release): https://github.com/siasia/livereload-extensions/downloads
#   Chrome https://chrome.google.com/webstore/detail/livereload/jnihajbhpnppcggbcgedagnkighmdlei
#
notification :off
interactor :off
logger :level => :info

guard 'livereload', :host => '127.0.0.1' do
  watch(%r{^templates/.+\.(css|js|html)$})
  watch(%r{^statics/.+\.(css|js|html)$})
  #watch(%r{.+\.(css|js|html|pyc)$})
end
