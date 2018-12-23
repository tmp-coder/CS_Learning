(* Dan Grossman, Coursera PL, HW2 Provided Code *)

(* if you use this function to compare two strings (returns true if the same
   string), then you avoid several of the functions in problem 1 having
   polymorphic types that may be confusing *)
fun same_string(s1 : string, s2 : string) =
    s1 = s2

(* put your solutions for problem 1 here *)

(* this is my helper function, passed a  option list x, then return [], or value of x*)
fun valof_lst x = 
    case x of
        NONE => []
        | SOME x => x



fun all_except_option(s,xs) =
    case xs of
       [] => NONE
     | x::xs' => if same_string(s,x)
                 then SOME xs'
                 else let val tl_val = all_except_option(s,xs')
                      in
                            case tl_val of
                               NONE => NONE
                             | SOME tl_val =>SOME  (x::tl_val)
                      end

fun get_substitutions1(xs,s)=
    case xs of
       [] => []
     | x::xs' => valof_lst(all_except_option(s,x))@get_substitutions1(xs',s)

(* this is a tail recursion version *)

fun get_substitutions2(xs,s) = 
    let 
        fun aux(xs,ret,s) =
            case xs of
               [] => ret
             | x::tail => aux(tail,valof_lst(all_except_option(s,x))@ret,s)
    in
        case xs of
           [] => []
         | x::xs' => aux(xs',valof_lst(all_except_option(s,x)),s)
    end

fun similar_names(xs,name : {first:string,middle: string,last:string}) = 
    let
        val {first,middle,last} = name
        val ret = [name]
        val first_lst = get_substitutions1(xs,first)
        fun reconstruct_name(first_candinate, ret)=
            case first_candinate of
               []=> ret
             | x::tl => let val parm = {first=x,middle=middle,last=last} 
                        in reconstruct_name(tl,parm::ret) 
                        end
    in
        reconstruct_name(first_lst,ret)
    end

(* you may assume that Num is always used with values 2, 3, ..., 10
   though it will not really come up *)
datatype suit = Clubs | Diamonds | Hearts | Spades   (*spades and clubs are black,
                                                      diamonds and hearts are red*)
datatype rank = Jack | Queen | King | Ace | Num of int 
type card = suit * rank

datatype color = Red | Black
datatype move = Discard of card | Draw 

exception IllegalMove

(* put your solutions for problem 2 here *)

(* One case-expression is enough. homework request  *)
fun card_color (s :suit, r : rank) = 
    case s of
       Spades  => Black
      | Clubs  =>Black
      | _ => Red

fun card_value_Ace (s : suit,r : rank,v) =
    case r of
       Ace => v
     | Num x => x
     | _  => 10

fun card_value (s :suit,r : rank) =
    card_value_Ace(s,r,11)

fun remove_card (cards_lst , cs,e ) =
    case cards_lst of
       [] => raise e
     | hd::tl => if hd = cs then tl
                 else hd :: remove_card(tl,cs,e)

fun all_same_color (cd_lst) =
    case cd_lst of
       x::y::tl => if (card_color x) = (card_color y) then all_same_color (y::tl)
                   else false 
     | _=> true


(* must use tail recursion
return sum of the value of the cards_list
  *)
fun sum_cards (cs_lst) = 
    let
        fun rc_sum(cs_lst, ret) =
              case cs_lst of
                 [] => ret
               | x::tl => rc_sum(tl,card_value(x)+ret)
    in
        rc_sum(cs_lst,0)
    end

(* Scoring works as follows: Let sum be the sum
of the values of the held-cards. If sum is greater than goal, the preliminary score is three times (sum-goal),
else the preliminary score is (goal - sum). The score is the preliminary score unless all the held-cards are
the same color, in which case the score is the preliminary score divided by 2 (and rounded down as usual
with integer division; use ML's div operator). psted from hw2.pdf *)

fun score_helper(sum :int,goal:int,same_color : bool)=
    let 
        val preliminary_score = if sum > goal  then 3 * (sum - goal)
                                else goal - sum
    in
        if same_color
        then preliminary_score div 2
        else preliminary_score
    end


fun score (cs_lst ,goal : int) =
    score_helper(sum_cards(cs_lst),goal,all_same_color (cs_lst))

(*helper function for officiate*)
fun aux_off(cl,ml : move list,goal,val_fun : card-> int,sc_fun: card list * int -> int ) =
    let
    (* assume Draw is llegal,that is cl is not empty*)
    fun next_state(hd_cards, cl, m : move,sum) =
        case m of
     Discard c =>(remove_card(hd_cards,c,IllegalMove), cl,sum - val_fun(c))
        | Draw => case cl of x::tl => (x::hd_cards,tl, sum +val_fun(x))
                            | _ => raise IllegalMove
    
    fun calc_ans(hl,cl,ml,sum) =
        if sum > goal
        then sc_fun(hl,goal)  (* sum > goal : over*)
        else
            case ml of
            [] => sc_fun(hl,goal)   (*empty move list,over*)
        | m::tl => case cl of
                    [] => sc_fun(hl,goal)(*empty cards list over*)
                    | _ => let val (r1,r2,s) = next_state(hl,cl,m,sum)
                           in calc_ans(r1,r2,tl,s)
                           end
    in
        calc_ans([],cl,ml,0)
    end

fun officiate(cl,ml,goal : int) =
    aux_off(cl,ml,goal,card_value,score)


(* Challenge problem *)

(* some helper function  *)

(*remove all duplicated card,for tail-recursion*)

(* given a cards list, return the number of Aces int cards list *)
fun num_of_Ace(cl) =
    let 
        fun tr_f(cl,ret)=
            case cl of
               [] => ret
             | x::tl => case x of
                            (_,Ace)   => tr_f(tl,1+ret)
                              | _ => tr_f(tl,ret)
    in
      tr_f(cl,0)
    end

fun score_challenge (cs_lst :card list ,goal : int) =
    let
        val na = num_of_Ace(cs_lst) 
        val sum= sum_cards(cs_lst) - 11*na (*value of Ace = 11*)
        (*given the number of ace which set value equal to 1,return the sum of crads*)
        fun aux_sum(one_of_ace) = sum + one_of_ace + (na - one_of_ace) * 11
        val same_color = all_same_color cs_lst
        fun min_score (now_ones,ret) = 
            let 
                val s = aux_sum(now_ones)
                val sc = score_helper(s,goal,same_color)
            in  
                if now_ones > na then ret
                else min_score(now_ones+1,Int.min(ret,sc))
            end

    in
        min_score(0,score_helper(sum + 11*na,goal,all_same_color(cs_lst)))
    end

fun officiate_challenge(cl,ml,goal : int) =
    let 
        fun my_card_val(s,r) =
            card_value_Ace(s,r,1)
    in
        aux_off(cl,ml,goal,my_card_val,score_challenge)
    end

