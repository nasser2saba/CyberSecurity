


# Drill - Decorators


## Exercise 1
_**Create a decorator that limits the execution of a function:**_

_When the function is executed too many times, an exception is thrown. The decorator must take one parameter, which is the number of times it is executed._


To create a decorator that limits the number of times a function can be executed, define a decorator that maintains a count of how many times the function has been called. If the function is called more times than the allowed limit, the decorator will raise an exception.



1. Define the decorator function that takes the maximum number of allowed executions as a parameter.
2. Inside the decorator, define a wrapper function that increments a call count and checks if the limit has been reached.
3. Raise an exception if the call count exceeds the limit.

**Implementation**

```python
class TooManyCallsException(Exception):
    pass

def limit_calls(max_calls):
    def decorator(func):
        call_count = 0

        def wrapper(*args, **kwargs):
            nonlocal call_count
            call_count += 1
            if call_count > max_calls:
                raise TooManyCallsException(f"Function '{func.__name__}' called too many times. Maximum allowed is {max_calls}.")
            return func(*args, **kwargs)

        return wrapper
    return decorator

# Example usage
@limit_calls(3)
def my_function():
    print("Function is running")

# Testing the decorator
try:
    my_function()  # First call
    my_function()  # Second call
    my_function()  # Third call
    my_function()  # This should raise an exception
except TooManyCallsException as e:
    print(e)
```

**Explanation**

1. **TooManyCallsException**: A custom exception class to indicate the function has been called too many times.
   
2. **limit_calls(max_calls)**: A decorator factory that takes the maximum number of allowed calls as a parameter and returns the actual decorator.

3. **decorator(func)**: The actual decorator function that wraps the target function.
   
4. **wrapper(args, kwargs)**: The wrapper function that increments the call count each time the function is called. If the call count exceeds the maximum allowed calls, it raises a `TooManyCallsException`. Otherwise, it calls the original function.

5. **@limit_calls(3)**: The example decorator usage limits the execution of `my_function` to 3 times.

**Testing**

The example usage demonstrates how the function `my_function` can be called up to 3 times. On the fourth call, it raises a `TooManyCallsException`.

You can run the provided script to see how the decorator works and how it enforces the call limit. Adjust the number of allowed calls and test with different functions as needed.

     
## Exercise 2
_**Create a decorator that controls what a function returns. The decorator must throw an exception if the function returns a string or an int.**_

To create a decorator that controls the return type of a function and throws an exception if the function returns a string or an integer, you can define a decorator that wraps the target function. After the function executes, the decorator checks the return type and raises an exception if the return type is either `str` or `int`.


1. Define a custom exception for handling invalid return types.
2. Create a decorator function that wraps the target function and checks its return type.
3. Raise the custom exception if the return type is not allowed.

**Implementation**

```python
class InvalidReturnTypeException(Exception):
    pass

def check_return_type(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, (str, int)):
            raise InvalidReturnTypeException(f"Function '{func.__name__}' returned an invalid type: {type(result).__name__}")
        return result
    return wrapper

# Example usage
@check_return_type
def example_function():
    return "This is a string"

@check_return_type
def another_example_function():
    return 42

@check_return_type
def valid_function():
    return [1, 2, 3]  # This should pass

# Testing the decorator
try:
    print(valid_function())  # This should work fine
    print(example_function())  # This should raise an exception
except InvalidReturnTypeException as e:
    print(e)

try:
    print(another_example_function())  # This should raise an exception
except InvalidReturnTypeException as e:
    print(e)
```

**Explanation**

1. **InvalidReturnTypeException**: A custom exception class to indicate the function returned an invalid type.
   
2. **check_return_type(func)**: The decorator function that wraps the target function.
   
3. **wrapper(*args, **kwargs)**: The wrapper function that calls the original function, checks its return type, and raises an `InvalidReturnTypeException` if the return type is either `str` or `int`.

4. **@check_return_type**: Example usage of the decorator applied to different functions.

**Testing**

The example demonstrates three functions:
- `valid_function`: Returns a list, which is allowed, so no exception is raised.
- `example_function`: Returns a string, which is not allowed, so an exception is raised.
- `another_example_function`: Returns an integer, which is not allowed, so an exception is raised.


     
## Exercise 3
_**A decorator that displays the time it took for the function to run (basic).**_


To create a decorator that measures and displays the time it takes for a function to run, you can use Python's `time` module. The decorator will record the start time before the function executes and the end time after the function completes, then calculate and print the elapsed time.


**Implementation**

```python
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()  # Record the end time
        elapsed_time = end_time - start_time  # Calculate the elapsed time
        print(f"Function '{func.__name__}' took {elapsed_time:.6f} seconds to run.")
        return result
    return wrapper

# Example usage
@timing_decorator
def example_function():
    time.sleep(2)  # Simulate a function that takes some time to run
    return "Function complete"

# Test the decorator
print(example_function())
```

**Explanation**

1. **timing_decorator(func)**: The decorator function that wraps the target function.
   
2. **wrapper(*args, **kwargs)**: The wrapper function that records the start and end times, calculates the elapsed time, and prints the result.
   
3. **start_time = time.time()**: Records the start time in seconds since the epoch.
   
4. **result = func(*args, **kwargs)**: Calls the original function and stores its result.
   
5. **end_time = time.time()**: Records the end time in seconds since the epoch.
   
6. **elapsed_time = end_time - start_time**: Calculates the time taken by the function.
   
7. **print(f"Function '{func.__name__}' took {elapsed_time:.6f} seconds to run.")**: Prints the name of the function and the elapsed time in seconds.

**Example Usage**

The example usage demonstrates a function `example_function` that simulates a delay using `time.sleep(2)` to mimic a function that takes some time to run. The `@timing_decorator` will measure and print the time taken by `example_function`.

**Running the Script**

When you run the provided script, you should see output similar to the following:

```
Function 'example_function' took 2.002345 seconds to run.
Function complete
```

This indicates the time it took for `example_function` to run and the return value of the function.
     