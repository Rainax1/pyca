# Casm

## Imporant
```asm
&refer *native*  
;; this line is imporant and should be in start of program
```

## Imports or Includes

```asm
&refer *native*::IO::{stdout, Read, Write}
&refer *native*::extra::{ myterminal, math, randomly as rand }
&refer *native*::os::path::Isfile

;; example.casm
&refer example
&refer example::testfunc 


Async @ True

```
## Consts
```asm
&const Float :: PI = 3.14

&const omega @ Days {
    Sun
    Mon
    Tue
}

omega {
    zero
    one
    two
}end

```
## Variables and DataTypes

```haskell
;; variable declaration and some data types

;; var datatype  :: variable_name = value
var Int :: y = 34
var Str :: name = "tom"
var Bool :: isTrue = True
var n = Null

;; Add Byte and One(char) DataType ,
;; One -> '' or 1 - Should be in Single quotes ,
;; Unity DataType only have 1 or ob1 and cannot be changed


;; List
var List :: list = .[1;2;True;'4']
var List<Int> :: intList = .[1;2;3]
var List<Str> :: strList = .["1";"2"]

var List:!4<Int, Str, Float, Bool> :: all = .[1,"two",2.0, True]

;; ImSeq or Tuple in python

;; Map
var Map :: test = .{
    
    "one" => 1 
    | "two" => 2;
    
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
    
    
}

var Map<String, Int> :: idk = .{

    "one" => 1
    "two" => 2

}


```
## Comments
```asm
! comment
;; comment
```
## Functions

```rust

// define fn -> defunc

// retInt :: defunc :: Int {
//    0, 100 rand::RandomInt
//}


defunc returnTrueFlase():: Bool {
   (True, False) rand::Choice ret
   
   ;; you can write it without rand::Choose 
   ;; (True, False) Choice ret
}

defunc forLoop() :: Void {
    var Int :: z = 10
    @for _ in z range {
        _ cwriteln
    }
    @endfor
    

}

defunc While() :: Void {

    @while 10 0 > do {
        10 cwriteln
    }
    @end

}

```ocaml

(*
    try {
        ;; code
 }
    rescue (Exception as e) {
        "Error: ", e ValueError panic

     }

*)
```


```

```asm
_start:

    defunc add(a :: Int, b :: Int) :: Int {

        a + b ret

    }

     list@1 cwriteln

    List[-2] = 1

    result = 3, 4 add

    @if (result == 7)  {

        "correct *\n", result cwriteln
    ;;  "correct *\n", {result} cwriteln,    you can also wrap variable with curly braces if you need more readability
    ;;                                       it will not change output

    } @else if (result ;= 6) {

        "idk" cwriteln
    } @else {

        "wrong: {result}\n" fcwriteln

    }

    @endif

    @if  returnTrueFlase() {
    ;; Can call function or class without any args using '()' after function
    
    
        "True" cwriteln
        0 drop          ;; drop is like exit() in  python

    }
    @else {

        "False" cwriteln
        1 drop
    }

    @endif


;; exit code will come after _end

_end:
    0 ret
```
