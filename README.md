Custom Assembly language
custom  language which transpile down to python

You can run it in 

- Interpreter Mode

    interpret file line by line
    
- Transpile Mode

    convert file to equivalent code of python

- Compile Mode

    compile file to executalble, ***need PyInstaller***

## Example Code

- Some language overview

## Imporant
```asm
%refer *native*  
;; this line is imporant and should be in start of program
```

## Imports or Includes

```asm
(from *native* refer IO.stdout)
(from *native* refer math)
(from *native* refer randomly as rand)

%include example.casm
%include testfunc from example.casm
```
## Consts
```asm
%const Float :: PI = 3.14

%const iota :: => Days {
    Sun
    Mon
    Tue
}
```
## Variables and DataTypes

```haskell
;; variable declaration and some data types

;; let datatype  :: variable_name = value
let Int :: y = 34
let Str :: name = "tom"
let Bool :: isTrue = True
let n = Nothing

;; Add Byte and One(char) DataType ,
;; One -> '' or 1 - Should be in Single quotes ,
;; Unity DataType only have 1 or ob1 and cannot be changed


;; List
let List :: list = .[1;2;True;'4']
let List<Int> :: intList = .[1;2;3]
let List<Str> :: strList = .["1";"2"]

let List:*4<Int, Str, Float, Bool> :: all = .[1,"two",2.0, True]

;; ImSeq or Tuple in python

;; Map
let Map :: test = .{
    
    "one" => 1;
    "two" => 2;
    
    ;; you can assign specific datatypes to both Key or Value
    
    Int :: 3 :: Str => "3";
    Float :: 4.0 :: Int => 4;
    Str :: "five" :: Float => 5.0;
    Str :: "isTrue" :: Bool => True
    
    ;; Key
    
    Str :: "stringValue" => 2 ;
    
    // datatype of value will be detected
    
    ;; Value
    
    "floatValue" :: Float => 3.0;
    
    // datatype of Key will be detected
    
    
    "itoa" => Iota; ;;  iota is a special built-in pre-declared identifier that simplifies the definition of incrementing constants
}

let Map<String, Int> :: idk = .{

    "one" => 1
    "two" => 2

}


Async = async :: => True
```
## Comments
```asm
! comment
;; comment
```
## Functions

```rust
fn returnTrueFlase() {
    return rand.choose(True, False)
}

fn forLoop() return Nothing {

    @for _ in z range {
        _ cwriteln
    }
    @endfor
    ret Nothing

}

fn While() -> Nothing {

    @while 10 0 > do {
        10 cwriteln
    }
    @end
    ret Nothing

}
```

```haskell
_start:

    fn add(a :: Int, b :: Int) return Int {
        ;; return Int , can be written as " -> Int "

        ret a + b

    }

     list@1 cwriteln

    List[-2] = 1

    result = add(4,3)

    @if (result == 7)  {

        "correct %d", result cwriteln

    } @else if (result ;= 6) {

        "idk" cwriteln
    } @else {

        "wrong *\n", result cwriteln

    }

    @endfi

    @if  returnTrueFlase() {
        "True" cwriteln
        drop 0            ;; drop is like exit() in  python

    }
    @else {

        "False" cwriteln
        drop 1
    }

    @endfi


;; exit code will come after _end

;; _end * ret 0

_end:
    ret 0
```