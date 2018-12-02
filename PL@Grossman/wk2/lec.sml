datatype mytype = TwoInts of int * int
                | Str of string
                | Pizza

fun f (x : mytype) = 
    case x of
       Pizza => 3
     | Str s => 8
     | TwoInts(i1,i2) => i1 + i2

(* expression tree *)

datatype exp = Constant of int
             | Negate of exp
             | Add of exp * exp
             | Mul of exp * exp

fun sum_int_list (xs : int list) = 
    case xs of [] => 0
        |x :: xs' => x + sum_int_list xs'

datatype ('a,'b) tree = Node of 'a * ('a,'b) tree * ('a,'b) tree
                      | Leaf of 'b

fun sum_tree ( tr : (int,int) tree) =
        case tr of
            Leaf i => i
            | Node(i,lft,rgt) => i + sum_tree (lft) + sum_tree(rgt)

fun f1 xs = 
    case xs of
       [] => []
     | _ => 1::xs

fun f2 [] = []
    | f2 _ = 1::xs
