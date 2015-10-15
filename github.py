from __future__ import print_function
import sys
import getopt
import urllib2
import base64
import json
import urlparse

class Github:

	def __init__(self):
		self.api_url = 'https://api.github.com/'

	def generate_token(self):
		# generate token for cli usage
		pass

	def add_token(self, token):
		self.token = token
		# or you could add already generated one
		pass

	def validate_token(self, token):
		pass

	def create_repo(self, repo_name):
		# create new repository
		pass

	def repo_exist(self, repo_name):
		# check if current repo is exist
		pass

	def fork_repo(self, repo_name):
		# repo name should be like drkraken/some-repo <username>/<reponame>
		# fork another user repo
		pass

	def delete_repo(self, repo_name):
		request = urllib2.Request(self.api_url + '/repos/' + repo_name)
		request.add_header('Authorization', 'token %s' % self.token)
		request.get_method = lambda: 'DELETE'
		try:
			result = urllib2.urlopen(request)
			print(result.info())
		except urllib2.HTTPError, e:
			if (e.code == 404):
				print('Can not find {0}'.format(repo_name))
			else:
				print(e)


class CLI:

	def __init__(self, argv):
		self.argv = argv
		self.username = 'unicorn'
		self.password = 'unicorn'

	def start(self):
		try:
			opts, args = getopt.getopt(self.argv, 'u:p:')
			self.pars_opts(opts)
			self.login_to_github()
		except getopt.GetoptError:
			self.print_help()
			sys.exit(2)

	def print_help(self):
		print('Usage:\n  github.py -u <username> -p <password>')

	def pars_opts(self, opts):
		for opt, val in opts:
			if opt == '-u':
				self.username = val
			elif opt == '-p':
				self.password = val

	def login_to_github(self):
		g = Github(self.username, self.password)
		g.connect()
		g.get_current_user()


if __name__ == '__main__':
	github = Github()
	github.delete_repo('drkraken/fly-csso')

