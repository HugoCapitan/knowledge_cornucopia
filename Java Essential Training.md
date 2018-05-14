# Notes for the Java 8 Essential Training Course

## Some general stuff.
Final keyword means once the var is set, it cannot be changed.  

    public static final FIRSTNAME = "hugo";  
Setting a var to null will dereference it and will be elegible for garbage collector.  

If no memory is available an OutOfMemoryException will be thrown.  

You can set available memory, check docs.  

Pass values to the main method from the console like this (they get passed to the args param:

    $ java Classname value1 value2 "value 3" etc... 

## Primitives
Lowercase  
Copied by value

- byte
- short
- int
- long
- boolean
- char

Helper classes for primitive values are usefull for example when casting to that type or other things, the helper classes are named like the data type they represent but Capitalized, except the int helper which is Integer.

Numeric Primitives always default to 0.

Be extremely careful with very small decimals and very big integers since they will lose precision, to avoid this, use java.math.BigDecimal and java.math.BigInteger

When casting to bigger values you can go implicit i.e. `long longValue = intValue;`

When casting to smaller types you need to explicitly cast: `byte byteVal = (byte) intValue`, if the int is bigger than the maxVal of int you lose data.

Literals for chars are wrapped in single quotes and Strings in double quotes

## Objects

Passed by reference, not value.

When compared, java checks if they are the very same object, not two identical objects.

Strings are basically an array of chars and are immutable, when "mutating" one in Java the value actually gets de-referenced and reassigned with the new val.

Compiler checks for matching strings when creating new ones and if it finds matches it references that match 

StringBuilder helps build strings, **Check why it exists** one reason might be to not create multiple String objects, I mean if you are paranoic about your memory

NumberFormat class is useful for formatting numbers in currency or decimal or ints

### Dates
    
    Date d = new Date();
    GregorianCalendar gc = new GregorianCalendar(1009, 1, 8)
    
months start at 0

check the date api, at least it's better than javascript's date api

### Dates in java 8

    java.time.LocalDate
    java.time.LocalTime
    java.time.LocalDateTime

months from 1 to 12

DateTimeFormatter to format stuff

## For Loops

Theres the everyday ugly for and **the cool way to do fors: (foreach)**

    // (vartype varname : arrayname)
    for (char c : stringVal) {
      // will iterate over each char of the string
    }


## Try catch and Exceptions

Exception is the master class of multiple types of exceptions.

You can add multiple catch blocks, each one looking for a different Exception Subclass.

Use `throw (new Exception("My custom message"));`
 get message with `e.getMessage()`

You can generate your own exceptions :O.

## Switch
Switch works with strings :3 (from java 7 +)

    switch(valueToExamine) {
      case valueToMatch:
        // code to execute
        break;
      // More cases
      default:
        // Code babe.
    }

## Methods

to receive an indetermined number of parameters: 

     static double addValues (String ... values) {
        // values is an array 
        for (String val : values) {
            // some code
        }
        return //a double
     }

## Arrays

Array utils `java.util.Arrays;`  
To copy: `System.arraycopy(orig, origStart, copy, copyStart, copyEnd);`

## ArrayLists and HashMaps

    List<Type> listname = new ArrayList<>();
    Map<KeyType, ValueType> mapname = new HashMap<>();

    listname.add(value);
    listname.get(index);
    listname.set(index, value);
    // etc...

    mapname.put(key, value);
    mapname.get(key);
    mapname.set(key, value);
    // etc...

### LIST: Using an iterator object

    import java.util.Iterator;

    Iterator<TypeOfValues> iterator = listToIterate.iterator();

    while (iterator.hasNext()) {
       String val = iterator.next();
       System.out.println(value);
    }

### LIST: Iterating the easy way

    for (Type value : list) {
      System.out.println(value);
    }

### LIST: The cool way :P

    // Passing a reference to a method of a class
    list.forEach(System.out::println);

### MAP: keySet iterator

    Set<String> keys = myMap.keySet(); // Getting set of unique keys.
    Iterator<String> iterator = keys.iterator();

    while(iterator.hasNext()) {
        String key = iterator.next();
        String value = myMap.get(key)
    }

### MAP: forEach
    
    Set<String> keys = myMap.keySet(); // Getting set of unique keys.

    for (String key : keys) {
      Sysyem.out.println(myMap.get(key));
    }

## Enums

Enums are a special kind of class.

    public enum EnumName {
      VALUEONE("value one"), VALUETWO("value two");

      private String name;

      EnumName(String name) {
          this.name = name;
      }

      // Override to string method
      @Override
      public String toString() {
          return name;
      }
    }

## The new io library

    import java.io.IOException;
    import java.nio.Path;
    import java.nio.Paths;
    import java.nio.Files; // utils for files
    import java.nio.StandardCopyOptions;
 
    Path sourcefile = Paths.get("files", "source.txt");
    Path targetfile = Paths.get("files", "target.txt");

    try {
        Files.copy(sourcefile, targetfile, StandardCopyOption.REPLACE_EXISTING);
    } catch (IOException) {
        e.printStackTrace();
    }


## An example on loading an url using buffers and more stuff

    import java.net.URL;

    // Declare outside try catch so they are available in finally
    InputStream stream = null;
    BufferedInputStream buf = null;

    try {
        URL url = new URl(url);
        stream = url.openStream();
        buf = new BufferedInputStream(stream);

        StringBuilder sb = new StringBuilder();

        // infinite loop
        while (true) {
            // If ok returns a numeric value, if wrong returns -1
            int data = buf.read();

            if (data == -1) {
                break;
            } else {
                sb.append((char) data);
            }

        }

        System.out.println(sb);
    } catch(IOException e) {
        e.pritStackTrace();
    } finally {
        // close stream and buffer
        stream.close();
        buf.close();
    }

