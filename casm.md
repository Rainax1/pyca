```javascript
%refer *native*  
;; this line is imporant and should be in start of program


(from *native* refer sys.stdout)
(from *native* refer random as rand)

%include example.casm
%include testfunc from example.casm

%const Float :: PI = 3.14

;; variable declaration and some data types


let Int :: y = 34
let Str :: name = "tom"
let Bool :: isTrue = True
let n = Nothing
let List :: list = .[1;2;3;4]

let Map :: test = .{
    
    "one" => 1;
    "two" => 2;
    
    ;; you can assign specific datatypes to both Key or Value
    
    Int :: 3 :: Str => "3";
    Float :: 4.0 :: Int => 4;
    Str :: "five" :: Float => 5.0;
    Str :: "isTrue" :: Bool => True
    
    ;; Key
    
    Str :: "stringValue" => 2;
    
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



! comment
;; comment


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

_end * ret 0
```
