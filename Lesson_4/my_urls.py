from views import index, about, contacts

my_urls = {
	'/': dict(path='/', name='Index', template_name='index.html', view=index()),
	'/my-about/': dict(path='/my-about/', name='About', template_name='about.html', view=about()),
	'/my-contacts/': dict(path='/my-contacts/', name='Contacts', template_name='contacts.html', view=contacts()),
}


# urlpatterns = [
# 	path('/', index(), 'name='index''),
# 	path('/about/', about(), name='about'),
# ]


# def url_parcer(url='/'):
# 	""" Get correct URL and Messoge (some text after '?=' in URL). """
#
# 	current_url_list = list(filter(lambda x: x, url.split('/')))
# 	# print('current_url_list', current_url_list)
# 	current_url = '/'
# 	message_from_url = ''
# 	for i in current_url_list:
# 		if i[0:2:] == '?=':
# 			message_from_url = i[2::]
# 			# print(message_from_url)
# 			i = ''
# 		else:
# 			current_url += f"{i.lower()}/"
# 	print('--(', current_url, ')--(', message_from_url, ')--', ' ---- data from url_parcer() function ----')
# 	return current_url, message_from_url
#
#
# if __name__ == '__main__':
# 	print(my_urls['/']['name'])
# 	try:
# 		print(my_urls['sfas'])
# 	except:
# 		print("KeyError: urls['sfas']")
# 	print(my_urls['/about/'].get('temtlate'))
#
# 	current_url = '/about/adfas/FGHHGFd/?=bcfwvhweiHHGDJ'
# 	print(url_parcer(current_url))
# 	current_url = '/'
# 	print(url_parcer(current_url))
# 	current_url = '/about//'
# 	print(url_parcer(current_url))
#
# # current_url = '/about/adfas/FGHHGFd/?=bcfwvhweiHHGDJ'
# # print(url_parcer(current_url))
# # current_url = '/'
# # print(url_parcer(current_url))
# # current_url = '/about//'
# # print(url_parcer(current_url))
