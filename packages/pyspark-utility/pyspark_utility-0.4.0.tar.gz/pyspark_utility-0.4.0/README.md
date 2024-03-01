# pyspark-utility
Provide utility functions for pyspark

## Example - How to use?
***
 ``` python
 from pyspark_utility.size_calculator import SizeCalculator 
 calc = SizeCalculator(spark) 
 calc.get_size_for_human(numbers) 
 ```

## Listing here are the modules that can be used highlighting some useful functions also (version - 0.4.0)
***
| Module           | Function                                       | Description                          |
|------------------|------------------------------------------------|--------------------------------------|
| _SizeCalculator_ | `get_size_for_machine(obj)`                    | get size in bytes                    |
| _SizeCalculator_ | `get_size_for_human(obj)`                      | get size in KB, MB, GB, and so on    |
| _FakeData_       | `fake_user()`, `fake_users(spark)`, and so on. | static functions to return fake data |