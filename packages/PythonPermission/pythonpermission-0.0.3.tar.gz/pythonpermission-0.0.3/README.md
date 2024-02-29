# PythonPermission

## Description

This package provide a simple way to manage element permissions in python. That is equivalent of the private, protected and protected access modifiers in other languages.

## Installation

```bash
pip install PythonPermission
```

## Usage

```python
from PythonPermission import private, fileprivate, protected, internal

class MyClass:
    def __init__(self):
        self.private_method()
        self.protected_method()
        self.fileprivate_method()
        self.internal_method()
        self.public_method()

    @private()
    def private_method(self):
        print("Private method")

    @protected()
    def protected_method(self):
        print("Protected method")

    @fileprivate()
    def fileprivate_method(self):
        print("Fileprivate method")
    
    @internal()
    def internal_method(self):
        print("Internal method")

    def public_method(self):
        self.private_method()
        self.protected_method()
        self.fileprivate_method()
        self.internal_method()
```

## License

GNU General Public License v3.0

## Author

- [Maxland255](https://pieteraerens.eu)
