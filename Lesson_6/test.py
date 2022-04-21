import functools


def greet(func):
	"""Приветствуем на английском."""

	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		val = func(*args, **kwargs)
		return "Hello " + val + "!"

	return wrapper


def flare(func):
	"""Кое-что добавим в нашу строку."""

	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		val = func(*args, **kwargs)
		return "🎉 " + val + " 🎉"

	return wrapper


@flare
@greet
def getname(name):
	return name



print(getname("Nafi"))