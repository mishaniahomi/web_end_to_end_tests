Запуск тестов
```
pytest -v --tb=line test_main_page.py
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