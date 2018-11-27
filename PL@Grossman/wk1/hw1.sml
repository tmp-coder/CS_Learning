(* is first date less then second date  *)
fun is_older(d1 : int * int * int, d2 : int * int * int) = 
    if (#1 d1) = (#1 d2)
    then 
        if (#2 d1) = (#2 d2)
        then (#3 d1) < (#3 d2)
        else (#2 d1) < (#2 d2)
    else (#1 d1) < (#1 d2)

fun number_in_month(dates : (int*int*int) list, month : int) = 
    if null dates
    then 0
    else 
        let val x = (if (#2 (hd dates)) = month then 1 else 0)
        in
            x + number_in_month(tl dates, month)
        end

fun number_in_months(dates : (int * int *int) list, months : int list) = 
    if null months
    then 0
    else number_in_month(dates,hd months) + number_in_months(dates,tl months)

fun dates_in_month (dates : (int * int * int) list, month : int) = 
    if null dates
    then []
    else 
        let 
            val x = hd dates
            val tl_lt = dates_in_month(tl dates,month) 
        in
            if (#2 x) = month
            then x :: tl_lt
            else tl_lt
        end
    
fun dates_in_months(dates :(int *int *int) list,months :int list) = 
    if null months
    then []
    else dates_in_month(dates,hd months)@(dates_in_months(dates,tl months))


(* need genetalize *)
fun get_nth_arbitray(lst : 'a list,nth : int) = 
    if nth = 1
    then hd lst
    else get_nth_arbitray(tl lst, nth -1)

fun get_nth(lst : string list, nth: int) =
    get_nth_arbitray(lst,nth)

fun date_to_string (date : int *int *int ) = 
    let 
        val months = ["January", "February", "March", "April",
                "May", "June", "July", "August", "September", 
                "October", "November", "December"]
    in
        get_nth(months,#2 date) ^" "^Int.toString(#3 date) ^ ", "^Int.toString(#1 date)
    end

(* assume the sum of entire lst  > the passed val,sum *)
fun number_before_reaching_sum( sum : int, int_lst : int list) = 
    if sum <= hd int_lst
    then 0
    else
        1 + number_before_reaching_sum(sum - (hd int_lst), tl int_lst)

(* assume year isn't leap year *)
fun what_month (days : int) = 
    let 
        val days_of_months = [31,28,31,30,31,30,31,31,30,31,30,31]
    in
        number_before_reaching_sum(days,days_of_months) +1
    end

fun month_range (day1 : int, day2 : int) = 
    if day1 > day2
    then []
    else
        what_month( day1) :: month_range(day1 +1,day2)
    

(* return the oldest dates  *)
fun oldest(dates : (int * int * int) list) = 
    if null dates
    then NONE
    else
        let
            val hd_date = hd dates
            val oldest_of_remain = oldest(tl dates)
        in
            if not (isSome oldest_of_remain)
            then SOME hd_date
            else if is_older(hd_date,valOf oldest_of_remain)
            then SOME hd_date
            else oldest_of_remain
        end

(* helper function,check a given lst contain a fixed value or not   *)
fun contain (value : int, lst : int list) = 
    if null lst
    then false
    else 
        if (hd lst) = value
        then true
        else contain(value,tl lst)


(* remove duplicate ele in a int list, 
    note the complicity of this algorithm is O(n^2) *)
fun remove_duplicate (lst : int list) = 
    if null lst
    then []
    else
        let
            val last_ele = remove_duplicate(tl lst)
        in
            if contain(hd lst,last_ele)
            then last_ele
            else (hd lst) :: last_ele
        end
(* like solutions to problems 3 and 5 except having a month in the second argument multiple
     times has no more effect than having it once. *)
fun number_in_months_challenge (dates : (int * int *int) list, months : int list)=
    let 
        val iso_months = remove_duplicate(months)
    in
        number_in_months(dates,iso_months)
    end

fun dates_in_months_challenge (dates :(int *int *int) list,months :int list) =
    let
        val iso_months = remove_duplicate(months)
    in
        dates_in_months(dates,iso_months)
    end

fun reasonable_date (year : int,month :int, day :int) =
    if year <=0
    then false
    else
        if month <=0 orelse month >12
        then false
        else
            let 
                val is_leap = ((year mod 400) =0) orelse 
                            ((year mod 4) =0 andalso (not ((year mod 100)=0)))
                val days_of_months = [31,28,31,30,31,30,31,31,30,31,30,31]
                val max_days = (if (month =2 andalso is_leap)
                                then 29
                                else get_nth_arbitray(days_of_months,month))
            in
                day >0 andalso day <= max_days
            end
