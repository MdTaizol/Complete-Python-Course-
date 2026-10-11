try:
	from importlib import import_module
	pyjokes = import_module("pyjokes")
except ImportError:
	raise ImportError("Install pyjokes in the active Python environment: python -m pip install pyjokes") from None
print("printing a joke from pyjokes...")
joke = pyjokes.get_joke()
print(joke)


"""
its my multiline
comment
"""