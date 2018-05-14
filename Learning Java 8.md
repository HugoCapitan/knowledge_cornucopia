# Java 8 (First Course) Notes

## Features

- Concurrency
- Class-based
- Object oriented
- Runs on Java Virtual Machine
- Incorporates a garbage collector

## UML

- minus sign = private
- plus sign = public
- Data inside classes should be private and be accessed via a getter or setter
- Class title -> atributes -> methods
- modifier aribute/method name (method params) : type

## Primitive data types
- char
- boolean
- Integers
  - byte
  - short
  - int
  - long
- float
- double

## Strings
An array or sequence of characters
Can be concatenated
Can be divided
Can be measured using the length method


## Casting types
Java gets weird with data types so in order to perform operations correctly you should either cast each value in the operation or make sure every part of it gets casted correctly, for example, when performing a calculation of the volume of a sphere this will happen:

Here the end result will be casted to a double since PI is a double, however the result is incorrect because the `4/3` operation returns a integer even though it should be a double, this is because that part of the equation was not casted

    double volume = 4/3 * Math.PI * 10*10*10;
    // 3141.5926...

The right way to do this would be, this time since `3.0` is a double, the division result will be casted and everything will be like flowers and amazing and stuff.

    double volume = 4/3.0 * Math.PI * 10*10*10;
    // 4188.7902...

## Loops

- do while (post test, this is runs at least once)
- while (pre test, checks condition at start)
- for (pre test)

## Parameters in methods
All primitive types are called by value, this is the value gets copied and then passed to the method, however, arrays and objects are passed by reference, so you get the original array inside of the method.

Be carefull with arrays

## Overloading
Two or more methods can have the same name as long as they accept different parameters or return a different type

# Array and ArrayList
So yeah, in java arrays and arraylists are different things, arrays can only hold primitive values and have a fixed size, while arraylists can hold objects and have and their size grows and shrinks dynamically

    // Array of 5 doubles
    Double[] doublesArr = new Double[5];

    // ArrayList of Movie objects
    import entertainment.Movie;
    import java.util.ArrayList;
    ArrayList<Movie> myFavourites = new ArrayList<Movies>();

ArrayList methods: 
- `.add(item)`
- `.remove(index)`
- `.get(index)`
- `.set(index)`
