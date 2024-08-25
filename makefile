lint:
	black app/
	isort app/

main:
	python main.py --debug