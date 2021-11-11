all: test

venv: .built/venv

.built/venv: .built/
	( \
		python3 -m venv venv ;\
		source venv/bin/activate ;\
		pip install --upgrade pip ;\
		pip install --upgrade -r requirements.txt ;\
		touch $@ ;\
	)

test: venv
	( \
		. venv/bin/activate ;\
		python3 setup.py install ;\
		luxa off ;\
		sleep 1 ;\
		luxa set --led=all ff0000 ;\
		sleep 1 ;\
		luxa set --led=all 00ff00 ;\
		sleep 1 ;\
		luxa set --led=all 0000ff ;\
		sleep 1 ;\
		luxa off ;\
	)

.built/:
	@mkdir -p $@

clean:
	rm -rf venv/
	rm -rf .built/
