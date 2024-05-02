# QA_Test_Stepik
There is a repo for final task on QA-course on stepik

Go to virtual environment:
```
source venv/bin/activate
```

To install dependencies run command:  
```
pip install -r requirements. txt
```

To start tests, run this commands: 
```commandline
pytest --browser_name=chrome --language=en test_product_page.py
pytest --browser_name=chrome --language=en test_main_page.py
```

To start marked tests for registration user and check some features, run this command:
```commandline
pytest -m registration --browser_name=chrome --language=en test_product_page.py
```

P.S. In pytest.ini file you can find markers for tests :)

Here is you can find certificate with honors: https://stepik.org/cert/2445236