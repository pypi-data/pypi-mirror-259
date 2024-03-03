# chromedriver-autoinstaller-fix

For the [botasaurus](https://github.com/omkarcloud/botasaurus) project, we utilize a modified version of [python-chromedriver-autoinstaller](https://github.com/yeongbin-jo/python-chromedriver-autoinstaller) that includes a few bug fixes:

- Correction of an `urllib3` error.
- Improvement in Chromedriver version detection for Windows.

## Installation

```bash
pip install chromedriver-autoinstaller-fix
```

## Usage
Just type `import chromedriver_autoinstaller_fix` in the module you want to use chromedriver.

## Example
```
from selenium import webdriver
import chromedriver_autoinstaller_fix


chromedriver_autoinstaller_fix.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
```

## Would appreciate a Star :)