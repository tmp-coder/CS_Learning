(* Coursera Programming Languages, Homework 3, Provided Code *)

exception NoAnswer


(* takes a string list and returns a string list that has only 
the strings in the argument that start with an uppercase letter.
 Assume all strings have at least 1 character. *)
fun only_capitals(str_lst) =
	List.filter(fn x => (Char.isUpper o String.sub)(x,0))  str_lst (*note for ME : List.filter is currying*)

(* takes a string list and returns the longest string in the
list. If the list is empty, return "". In the case of a tie, 
return the string closest to the beginning of the list. *)
fun longest_string1 str_lst =
	List.foldl (fn (x,acc) => if String.size x > String.size acc
							 then x else acc) "" str_lst

(* like longest_string1 except in the case of ties
it returns the string closest to the end of the list. *)
fun longest_string2 str_lst =
	List.foldl (fn (x,acc) => if String.size x >= String.size acc
							 then x else acc) "" str_lst

(* passed a function that behaves like > (so it returns true exactly
when its rst argument is stricly greater than its second), then the function returned has the same
behavior as longest_string1. *)
fun longest_string_helper f str_lst =
	List.foldl (fn (x,acc) => (if (f(String.size x,String.size acc)) then x else acc)) "" str_lst

val longest_string3 = longest_string_helper (fn (x,y)=> x>y)

val longest_string4 = longest_string_helper (fn (x,y) => x>=y)

(* takes a string list and returns the longest string in
the list that begins with an uppercase letter, or "" if there are no such strings. Assume all strings
have at least 1 character. *)
val longest_capitalized = (longest_string1 o only_capitals)


(* takes a string and returns the string that is the same characters in
reverse order *)
fun rev_string str =
	(String.implode o rev o String.explode) str

fun first_answer f lst =
	case lst of
	   [] => raise NoAnswer
	 | x::xs' => case (f x) of
		SOME v => v
	  | NONE => first_answer f xs'

fun all_answers f lst =
	case lst of
	   []  => SOME []
	 | h::t => case (f h) of
				NONE => NONE
	  		 | SOME v => let val ret = (all_answers f t)
			   			in
							case ret of
								NONE => NONE
							| 	SOME x=> SOME (v@x)
						end

datatype pattern = Wildcard
		 | Variable of string
		 | UnitP
		 | ConstP of int
		 | TupleP of pattern list
		 | ConstructorP of string * pattern

datatype valu = Const of int
	      | Unit
	      | Tuple of valu list
	      | Constructor of string * valu

fun g f1 f2 p =
    let 
	val r = g f1 f2 
    in
	case p of
	    Wildcard          => f1 ()
	  | Variable x        => f2 x
	  | TupleP ps         => List.foldl (fn (p,i) => (r p) + i) 0 ps
	  | ConstructorP(_,p) => r p
	  | _                 => 0
    end

fun my_g f1 f2 p =
    let 
	val r = my_g f1 f2 
    in
	case p of
	    Wildcard          => f1 ()
	  | Variable x        => f2 x
	  | TupleP ps         => List.foldl (fn (p,i) => (r p)@ i) [] ps
	  | ConstructorP(_,p) => r p
	  | _                 => []
    end

val count_wildcards = g (fn ()=>1) (fn s=>0)

val count_wild_and_variable_lengths = g (fn ()=>1) (fn s => String.size s)

fun count_some_var (s,p) = g (fn ()=>0) (fn x => if x=s then 1 else 0) p

val val_lst = my_g (fn ()=>[]) (fn s=>[s])

(* (code from https://stackoverflow.com/questions/10033165/find-if-duplicates-exist-sml-nj?noredirect=1&lq=1) *)
fun duplicated [] = false
  | duplicated (x::xs) = (duplicated xs) orelse (List.exists (fn y => x = y) xs) 

fun check_pat p = not ((duplicated o val_lst) p)
(**** for the challenge problem only ****)

fun match(v,p) = 
	case (v,p) of
	   (_,Wildcard) => SOME []
	 | (_,Variable s) => SOME [(s,v)] (*note :Wild cards are used for pattern matching only.
	 								 They can not be used as expressions 
									as they do not evaluate to a value. from 
									https://stackoverflow.com/questions/27956403/wild-cards-in-sml*)
	 | (Unit,UnitP) => SOME []
	 | (Const i1,ConstP i2) => if i1 = i2 then SOME [] else NONE
	 | (Constructor (s1,v), ConstructorP(s2,p)) => if s1 = s2 then match(v,p) else NONE
	 | (Tuple vs,TupleP ps) => if (List.length vs  = List.length ps) then all_answers match (ListPair.zip(vs,ps)) else NONE
	 | (_,_) => NONE

fun first_match v lst = 
	(SOME (first_answer (fn x => match (v,x)) lst )) handle NoAnswer => NONE


datatype typ = Anything
	     | UnitT
	     | IntT
	     | TupleT of typ list
	     | Datatype of string

(**** you can put all your code here ****)