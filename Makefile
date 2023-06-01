build:
	python3 -m build

push:
	twine upload -r testpypi dist/*

buildp:
	python3 -m build && twine upload -r testpypi dist/*

clear:
	rm -r dist src/baboo_game.egg-info