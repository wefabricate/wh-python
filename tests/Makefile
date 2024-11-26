

test_pydantic1:
	python -m venv venv1
	. venv1/bin/activate; pip install -r requirements_pydantic1.txt; pip install ../build/*-py3-none-any.whl ;pytest --api_url ${API_URL} --auth_url ${AUTH_URL} --client_id ${API_CLIENT_ID} --client_secret ${API_CLIENT_SECRET} --user ${API_USER} --password ${API_PASSWORD} --junitxml=out/output_pydantic1.xml --html=out/report_pydantic1.html --self-contained-html; deactivate

test_pydantic2:
	python -m venv venv2
	. venv2/bin/activate; pip install -r requirements_pydantic2.txt; pip install ../build/*-py3-none-any.whl; pytest --api_url ${API_URL} --auth_url ${AUTH_URL} --client_id ${API_CLIENT_ID} --client_secret ${API_CLIENT_SECRET} --user ${API_USER} --password ${API_PASSWORD} --junitxml=out/output_pydantic2.xml --html=out/report_pydantic2.html --self-contained-html; deactivate

tests: test_pydantic1 test_pydantic2


clean:
	rm -r venv1 venv2 out
