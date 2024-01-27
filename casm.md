```C
%refer *native*  
;; this line is imporant and should be in start of program


(from *native* refer sys.stdout)
(from *native* refer random as rand)

%include example.casm
%include testfunc from example.casm

%const float: PI = 3.14

;; variable declaration and some data types

let int: y = 34
let str: name = "tom"
let n = Nothing
let list: List = <1;2;3;4>

let dict: test = {

    a = iota ;; reserved keyword like iota in go lang
    b = iota

}


! comment
;; comment

fn globalFunc(a: int) -> int {
    ret a
}

fn returnTrueFlase() {
    return rand.choose(True, False)
}

fn forLoop() return Nothing {

    %for _ in (z)range {
        (z)writeln
        ret Nothing
    }
    %endfor

}



_start:

    ! this function is not available outside &start

    fn add(a: int, b:int) return int {
        ;; return int , can be written as -> int

        ret a + b

    }

    (List@1)writeln

    List[-2] = 1

    result = add(4,3)

    @if (result == 7)  {

        ("correct %d", result)writeln

    } @else if (result ;= 6) {

        ("idk")writeln
    } @else {

        ("wrong %d", result)

    }

    @endfi

    @if  returnTrueFlase() {
        ("True")writeln
        drop 0            ;; drop is like exit() in  python

    }
    @else {

        ("False")writeln
        drop 1
    }

    @endfi


;; exit code will come after _end

_end * ret 0
```
