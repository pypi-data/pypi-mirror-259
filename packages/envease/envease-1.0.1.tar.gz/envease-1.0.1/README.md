# EnvEase
[Persian Immortal Studios](https://github.com/Persian-Immortal) presents, A Python package to easily work with environment variables, inspired by the method used in [Laravel](https://github.com/laravel/laravel) framework to read the `.env` file. 

## Installation
You can install `envease` via pip:
```bash
pip install envease
```

## Usage
if you only want to use a single `.env` file where the python file is located then you can import the package like this:
```py
from envease import env
```
then the usage is gonna be simple:
```bash
# inside the .env file
KEY="Hello, World"
```
```py
print(env('KEY')) # prints the "Hello, World" message
```
---
else if you want to use other environment variable files than `.env` you can use the package like this:
```py
from envease import *

load_env_file('file_name')
print('KEY') # this prints the value inside the 'KEY' inside the 'file_name' file
```
---
you can even dynamically call different environment variable files
```py
from envease import *
env_files = {
    "first": ".first.env",
    "second": ".second.env",
    "third": ".third.env",
}

load_multiple(env_files)

print(dynamic_env('first', 'KEY')) # this will print the value addressed with 'KEY' inside the .first.env file
```
> ***Notice:*** you can as well handle default values if the returned value is null!
```py
print('KEY', 'default value') # this prints the value addressed with 'KEY' inside the environment variables. if it was null it will print 'default value' as a string
print(dynamic_env('first', 'KEY'), 'default value') # this prints the value addressed with 'KEY' inside the environment variables addressed with 'first' key in the dictionary. if it was null it will print 'default value' as a string
```

---

# Contributing
Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please [open an issue](https://github.com/Persian-Immortal/envease/issues/new) or submit a pull request.

# License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.