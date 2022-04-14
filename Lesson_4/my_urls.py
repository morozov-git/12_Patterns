from views import Index, About, Contacts

my_urls = {
	'/': dict(path='/', name='Index', template_name='index.html', view=Index()),
	'/my-about/': dict(path='/my-about/', name='About', template_name='about.html', view=About()),
	'/my-contacts/': dict(path='/my-contacts/', name='Contacts', template_name='contacts.html', view=Contacts()),
}

