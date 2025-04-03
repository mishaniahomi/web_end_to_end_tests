Запуск тестов
```
pytest -v --tb=line test_main_page.py
```
Вывод
```
(web-test-py3.12) homi@homi-VirtualBox:~/myprojects/web-test$ pytest -v --tb=line test_main_page.py
====================================================================================== test session starts =======================================================================================
platform linux -- Python 3.12.3, pytest-8.3.5, pluggy-1.5.0 -- /home/homi/.cache/pypoetry/virtualenvs/web-test-e05s1Tt6-py3.12/bin/python
cachedir: .pytest_cache
rootdir: /home/homi/myprojects/web-test
configfile: pyproject.toml
plugins: base-url-2.1.0, playwright-0.7.0
collected 2 items                                                                                                                                                                                

test_main_page.py::test_guest_can_go_to_login_page PASSED                                                                                                                                  [ 50%]
test_main_page.py::test_quest_should_be_input_username PASSED                                                                                                                              [100%]

======================================================================================= 2 passed in 5.68s ========================================================================================
(web-test-py3.12) homi@homi-VirtualBox:~/myprojects/web-test$ 
```

Скачать версию 
```
wget https://chromedriver.storage.googleapis.com/130.0.6723.91/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
```
Переместите разархивированный файл с СhromeDriver в нужную папку и разрешите запускать chromedriver как исполняемый файл:
```
sudo mv chromedriver /usr/local/bin/chromedriver
sudo chown root:root /usr/local/bin/chromedriver
sudo chmod +x /usr/local/bin/chromedriver
```