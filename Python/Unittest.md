

# Drills - unit testing
Now that you have the basics, let's do some drills!

Create a unittest for each of these functions.

Custom exception
We define here some custom exception.


class InvalidArgumentException(Exception):
    """Raised when a param is invalid."""

    pass
     

```python 
class InvalidArgumentException(Exception):
    """Raised when a param is invalid."""
    pass

def addition(number_one: int, number_two: int) -> int:
    if not isinstance(number_one, int) or not isinstance(number_two, int):
        raise InvalidArgumentException("A parameter is not an int!")
    return number_one + number_two
```


## Addition
Check the result for those arguments:

[1, 1]
[2, 3]
[5, 2]
[20, 4]
[0, 200]
[2999, 231234]
[0, 0]



```python 
import unittest

class TestAdditionFunction(unittest.TestCase):
    def test_addition_valid_inputs(self):
        test_cases = [
            (1, 1, 2),
            (2, 3, 5),
            (5, 2, 7),
            (20, 4, 24),
            (0, 200, 200),
            (2999, 231234, 234233),
            (0, 0, 0)
        ]
        
        for number_one, number_two, expected in test_cases:
            with self.subTest(f"{number_one} + {number_two} = {expected}"):
                self.assertEqual(addition(number_one, number_two), expected)
    
    def test_addition_invalid_inputs(self):
        invalid_inputs = [
            ("string", 1),
            (1, "string"),
            (1.5, 2),
            (2, 1.5),
            ({}, 1),
            (1, {}),
            ([], 1),
            (1, [])
        ]
        
        for number_one, number_two in invalid_inputs:
            with self.subTest(f"addition({number_one}, {number_two}) raises InvalidArgumentException"):
                with self.assertRaises(InvalidArgumentException):
                    addition(number_one, number_two)

if __name__ == '__main__':
    unittest.main()

```



In addition, create a test that checks that InvalidArgumentException is raised correctly if you give something else than an int to the function. Check for: string, float, dict, list


def addition(number_one: int, number_two: int) -> int:
    if not isinstance(number_one, int) or not isinstance(number_two, int):
        raise InvalidArgumentException("A parameter is not an int!")
    return number_one + number_two
     
```python
import unittest

class InvalidArgumentException(Exception):
    """Raised when a param is invalid."""
    pass

def addition(number_one: int, number_two: int) -> int:
    if not isinstance(number_one, int) or not isinstance(number_two, int):
        raise InvalidArgumentException("A parameter is not an int!")
    return number_one + number_two

class TestAdditionFunction(unittest.TestCase):
    def test_addition_valid_inputs(self):
        test_cases = [
            (1, 1, 2),
            (2, 3, 5),
            (5, 2, 7),
            (20, 4, 24),
            (0, 200, 200),
            (2999, 231234, 234233),
            (0, 0, 0)
        ]
        
        for number_one, number_two, expected in test_cases:
            with self.subTest(f"{number_one} + {number_two} = {expected}"):
                self.assertEqual(addition(number_one, number_two), expected)
    
    def test_addition_invalid_inputs(self):
        invalid_inputs = [
            ("string", 1),
            (1, "string"),
            (1.5, 2),
            (2, 1.5),
            ({}, 1),
            (1, {}),
            ([], 1),
            (1, [])
        ]
        
        for number_one, number_two in invalid_inputs:
            with self.subTest(f"addition({number_one}, {number_two}) raises InvalidArgumentException"):
                with self.assertRaises(InvalidArgumentException):
                    addition(number_one, number_two)

if __name__ == '__main__':
    unittest.main()

```

_Explanation_
1. Valid Input Tests:

- The test_addition_valid_inputs method tests the addition function with valid integer inputs. It uses a list of tuples, where each tuple contains two integers to add and the expected result.
- The with self.subTest construct allows each case to be tested separately, providing clearer output on which case failed if any.

2. Invalid Input Tests:

- The test_addition_invalid_inputs method tests the addition function with various invalid inputs to ensure that InvalidArgumentException is raised appropriately.
- The invalid_inputs list contains tuples of invalid inputs, including strings, floats, dictionaries, and lists.
- The with self.subTest construct is again used for better test reporting.
- The self.assertRaises context manager is used to check if the exception is raised.


     
## Substraction 
Check the result for those arguments:

[1, 1]
[2, 3]
[5, 2]
[20, 4]
[0, 200]
[2999, 231234]
[0, 0]


In addition, create a test that checks that InvalidArgumentException is raised correctly if you give something else than an int to the function. Check for: string, float, dict, list.


def substraction(number_one: int, number_two: int) -> int:
    if not isinstance(number_one, int) or not isinstance(number_two, int):
        raise InvalidArgumentException("A param is not an int!")
    return number_one - number_two
     


script: 

Let's first define the `subtraction` function and the `InvalidArgumentException` exception class. Then, we'll write the unit tests for this function, including tests for valid and invalid inputs.

- Function and Exception Definition


```python
class InvalidArgumentException(Exception):
    """Raised when a param is invalid."""
    pass

def subtraction(number_one: int, number_two: int) -> int:
    if not isinstance(number_one, int) or not isinstance(number_two, int):
        raise InvalidArgumentException("A parameter is not an int!")
    return number_one - number_two
```

- Unit Tests


```python
import unittest

class TestSubtractionFunction(unittest.TestCase):
    def test_subtraction_valid_inputs(self):
        test_cases = [
            (1, 1, 0),
            (2, 3, -1),
            (5, 2, 3),
            (20, 4, 16),
            (0, 200, -200),
            (2999, 231234, -228235),
            (0, 0, 0)
        ]
        
        for number_one, number_two, expected in test_cases:
            with self.subTest(f"{number_one} - {number_two} = {expected}"):
                self.assertEqual(subtraction(number_one, number_two), expected)
    
    def test_subtraction_invalid_inputs(self):
        invalid_inputs = [
            ("string", 1),
            (1, "string"),
            (1.5, 2),
            (2, 1.5),
            ({}, 1),
            (1, {}),
            ([], 1),
            (1, [])
        ]
        
        for number_one, number_two in invalid_inputs:
            with self.subTest(f"subtraction({number_one}, {number_two}) raises InvalidArgumentException"):
                with self.assertRaises(InvalidArgumentException):
                    subtraction(number_one, number_two)

if __name__ == '__main__':
    unittest.main()
```


_Explanation:_

1. **Valid Input Tests**:
   - The `test_subtraction_valid_inputs` method tests the `subtraction` function with valid integer inputs. It uses a list of tuples, where each tuple contains two integers to subtract and the expected result.
   - The `with self.subTest` construct allows each case to be tested separately, providing clearer output on which case failed if any.

2. **Invalid Input Tests**:
   - The `test_subtraction_invalid_inputs` method tests the `subtraction` function with various invalid inputs to ensure that `InvalidArgumentException` is raised appropriately.
   - The `invalid_inputs` list contains tuples of invalid inputs, including strings, floats, dictionaries, and lists.
   - The `with self.subTest` construct is again used for better test reporting.
   - The `self.assertRaises` context manager is used to check if the exception is raised.


## Devision 
Here is a function that returns a float and can take a float or an int as parameter.

Create a test that will check the result of those arguments:

[1, 1]
[2, 3]
[5, 2]
[20, 4]
[0, 200]
[2999, 231234]
[0, 0]
[5, 0]
[5, "9"]
[5, [1, 2]]
[2, {"param2": 2}]
For each parameter, check that the result is the expected type (a string if one the arguments is bad, otherwise a float).


from typing import Union


def divide(
    number_one: Union[int, float], number_two: Union[int, float]
) -> Union[float, str]:
    try:
        result = number_one / number_two
    except ZeroDivisionError:
        result = "You can't divide by zero!"
    except Exception as ex:
        result = f"An argument is not an int or a float! -> {ex}"

    return result
     



- Function and Exception Definition

First, we define the `divide` function:

```python
from typing import Union

def divide(number_one: Union[int, float], number_two: Union[int, float]) -> Union[float, str]:
    try:
        result = number_one / number_two
    except ZeroDivisionError:
        result = "You can't divide by zero!"
    except Exception as ex:
        result = f"An argument is not an int or a float! -> {ex}"
    return result
```

- Unit Tests

Next, we create the unit tests for the `divide` function:

```python
import unittest

class TestDivideFunction(unittest.TestCase):
    def test_divide_valid_inputs(self):
        test_cases = [
            (1, 1, 1.0),
            (2, 3, 2/3),
            (5, 2, 2.5),
            (20, 4, 5.0),
            (0, 200, 0.0),
            (2999, 231234, 2999/231234),
            (0, 0, "You can't divide by zero!"),
            (5, 0, "You can't divide by zero!"),
        ]
        
        for number_one, number_two, expected in test_cases:
            with self.subTest(f"{number_one} / {number_two} = {expected}"):
                result = divide(number_one, number_two)
                if isinstance(expected, str):
                    self.assertEqual(result, expected)
                else:
                    self.assertAlmostEqual(result, expected, places=7)

    def test_divide_invalid_inputs(self):
        invalid_inputs = [
            (5, "9"),
            (5, [1, 2]),
            (2, {"param2": 2}),
        ]
        
        for number_one, number_two in invalid_inputs:
            with self.subTest(f"divide({number_one}, {number_two}) raises an error message"):
                result = divide(number_one, number_two)
                self.assertIsInstance(result, str)
                self.assertIn("An argument is not an int or a float!", result)

if __name__ == '__main__':
    unittest.main()
```

_Explanation_

1. **Valid Input Tests**:
   - The `test_divide_valid_inputs` method tests the `divide` function with valid inputs, including edge cases like division by zero.
   - The `test_cases` list contains tuples of inputs and the expected result.
   - For valid divisions, the `self.assertAlmostEqual` method is used to compare floating-point results, allowing for small differences due to floating-point arithmetic.
   - For divisions that should result in an error message (e.g., division by zero), `self.assertEqual` is used to check the error message.

2. **Invalid Input Tests**:
   - The `test_divide_invalid_inputs` method tests the `divide` function with various invalid inputs to ensure that an appropriate error message is returned.
   - The `invalid_inputs` list contains tuples of invalid inputs.
   - The `self.assertIsInstance` method checks that the result is a string.
   - The `self.assertIn` method checks that the error message contains the expected text.


     
## File Handling 
Create a function create_and_delete_test_file() that creates a new file named test.txt, adds 'this is a text' in it then deletes the file.
Create a test that checks if the file is well created.
Create a test to check that the content of the file is 'this is a text'. You will need to find a way to prevent the function to delete the file during this specific test.
Create a test to check that the function deletes the file.

```python 
# Create create_and_delete_test_file()
def create_and_delete_test_file():
    pass
```
     

Here’s how you can implement the `create_and_delete_test_file` function and the corresponding unit tests.

- Function Implementation

```python
import os

def create_and_delete_test_file():
    filename = 'test.txt'
    with open(filename, 'w') as f:
        f.write('this is a text')
    os.remove(filename)
```

- Unit Tests

You can use the `unittest` framework to create the tests. To prevent the function from deleting the file during the content check, you can mock the `os.remove` method.

```python
import unittest
import os
from unittest.mock import patch

class TestFileHandling(unittest.TestCase):
    def test_file_creation(self):
        # Run the function
        create_and_delete_test_file()
        # Check if the file was created
        self.assertFalse(os.path.exists('test.txt'), "File should not exist after deletion")

    @patch('os.remove')
    def test_file_content(self, mock_remove):
        # Run the function but prevent deletion
        create_and_delete_test_file()
        # Check if the file was created
        self.assertTrue(os.path.exists('test.txt'), "File should exist")
        # Check the content of the file
        with open('test.txt', 'r') as f:
            content = f.read()
        self.assertEqual(content, 'this is a text', "File content mismatch")
        # Clean up the file manually since it wasn't deleted
        os.remove('test.txt')

    def test_file_deletion(self):
        # Create a file manually
        with open('test.txt', 'w') as f:
            f.write('this is a text')
        # Check that the file exists
        self.assertTrue(os.path.exists('test.txt'), "File should exist before deletion")
        # Run the function
        create_and_delete_test_file()
        # Check that the file was deleted
        self.assertFalse(os.path.exists('test.txt'), "File should be deleted")

if __name__ == '__main__':
    unittest.main()
```

_Explanation_

1. **Function Implementation**:
   - The `create_and_delete_test_file` function creates a file named `test.txt`, writes the string `'this is a text'` to it, and then deletes the file.

2. **Test Class**:
   - **test_file_creation**: Ensures that the file does not exist after the function runs, indicating it was created and then deleted.
   - **test_file_content**: Uses the `patch` decorator from `unittest.mock` to mock `os.remove` to prevent the file from being deleted during the test. This allows checking the file's existence and its content.
   - **test_file_deletion**: Manually creates a file, verifies its existence, runs the function, and then checks that the file was deleted.

3. **Test Execution**:
   - To run the tests, save the test code to a file (e.g., `test_file_handling.py`) and execute it with the `unittest` command:
     ```sh
     python -m unittest test_file_handling.py
     ```

This setup will ensure that all aspects of the file handling function are tested, including creation, content verification, and deletion.


    
_**You might have noticed that it is quite difficult to make the unit tests work for such a complicated function. How about separating the concern and creating separate functions for each particular action ?**_



Separating concerns into different functions will make the code easier to test and maintain. We can create three separate functions: one for creating the file, one for writing to the file, and one for deleting the file. Then, we can test each function individually.

- Function Implementation

1. **Creating the file:**
2. **Writing to the file:**
3. **Deleting the file:**

```python
import os

def create_file(filename: str):
    with open(filename, 'w') as f:
        pass

def write_to_file(filename: str, content: str):
    with open(filename, 'w') as f:
        f.write(content)

def delete_file(filename: str):
    os.remove(filename)

def create_and_delete_test_file():
    filename = 'test.txt'
    create_file(filename)
    write_to_file(filename, 'this is a text')
    delete_file(filename)
```

- Unit Tests

Now, we can create unit tests for each of these functions.

```python
import unittest
import os

class TestFileHandling(unittest.TestCase):
    def test_create_file(self):
        filename = 'test.txt'
        create_file(filename)
        self.assertTrue(os.path.exists(filename), "File should be created")
        os.remove(filename)  # Clean up

    def test_write_to_file(self):
        filename = 'test.txt'
        create_file(filename)
        write_to_file(filename, 'this is a text')
        with open(filename, 'r') as f:
            content = f.read()
        self.assertEqual(content, 'this is a text', "File content mismatch")
        os.remove(filename)  # Clean up

    def test_delete_file(self):
        filename = 'test.txt'
        create_file(filename)
        write_to_file(filename, 'this is a text')
        self.assertTrue(os.path.exists(filename), "File should exist before deletion")
        delete_file(filename)
        self.assertFalse(os.path.exists(filename), "File should be deleted")

    def test_create_and_delete_test_file(self):
        create_and_delete_test_file()
        self.assertFalse(os.path.exists('test.txt'), "File should not exist after deletion")

if __name__ == '__main__':
    unittest.main()
```

Explanation

1. **Function Implementation**:
   - `create_file`: Creates a file with the specified name.
   - `write_to_file`: Writes the specified content to the file.
   - `delete_file`: Deletes the specified file.
   - `create_and_delete_test_file`: Combines the above functions to create, write to, and delete the file.

2. **Test Class**:
   - **test_create_file**: Tests the `create_file` function to ensure the file is created.
   - **test_write_to_file**: Tests the `write_to_file` function to ensure the correct content is written to the file.
   - **test_delete_file**: Tests the `delete_file` function to ensure the file is deleted.
   - **test_create_and_delete_test_file**: Tests the `create_and_delete_test_file` function to ensure the file is created, written to, and deleted correctly.

3. **Test Execution**:
   - To run the tests, save the test code to a file (e.g., `test_file_handling.py`) and execute it with the `unittest` command:
     ```sh
     python -m unittest test_file_handling.py
     ```

