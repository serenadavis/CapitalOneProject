(* 
                         CS 51 Problem Set 4
                 A Language for Symbolic Mathematics
                               Testing
 *)

open Expression ;;
open ExpressionLibrary ;;
open Absbook ;; 

let contains_var_test () =
  unit_test (contains_var (parse "x")) "contains_var just var";
  unit_test (contains_var (parse "x+3")) "contains_var sum left";
  unit_test (contains_var (parse "4+x")) "contains_var sum right";
  unit_test (contains_var (parse "x*3")) "contains_var mult left";
  unit_test (contains_var (parse "4*x")) "contains_var mult right";
  unit_test (contains_var (parse "x/3")) "contains_var div left";
  unit_test (contains_var (parse "4/x")) "contains_var div right";
  unit_test (contains_var (parse "x-3")) "contains_var subtract left";
  unit_test (contains_var (parse "4-x")) "contains_var subtract right";
  unit_test (contains_var (parse "x^4")) "contains_var pow left";
  unit_test (contains_var (parse "19^x")) "contains_var pow right";
  unit_test (contains_var (parse "sin x")) "contains_var sin";
  unit_test (contains_var (parse "cos x")) "contains_var cos";
  unit_test (contains_var (parse "ln x")) "contains_var ln";
  unit_test (contains_var (parse "~ x")) "contains_var neg";
  unit_test (contains_var (parse "15+(3+x)"))
    "contains_var binop nested in binop";
  unit_test (contains_var (parse "15+(~x)"))
    "contains_var unop nested in binop";
  unit_test (contains_var (parse "~(sin x)"))
    "contains_var unop nested in unop";
  unit_test (contains_var (parse "~(x+14)"))
    "contains_var binop nested in unop";
  unit_test (not (contains_var (parse "2"))) "contains_var number";
  unit_test (not (contains_var (parse "3+4"))) "contains_var sum only numbers";
  unit_test (not (contains_var (parse "4*51")))
    "contains_var mult only numbers";
  unit_test (not (contains_var (parse "4/3"))) "contains_var div only numbers";
  unit_test (not (contains_var (parse "17-3")))
    "contains_var subtract only numbers";
  unit_test (not (contains_var (parse "2^4")))
    "contains_var pow only numbers";
  unit_test (not (contains_var (parse "sin 1")))
    "contains_var sin";
  unit_test (not (contains_var (parse "cos 0")))
    "contains_var only numbers";
  unit_test (not (contains_var (parse "ln 10")))
    "contains_var ln only numbers";
  unit_test (not (contains_var (parse "~ 17")))
    "contains_var neg only numbers";;
  
let evaluate_test () =
  unit_test (evaluate (parse "x") 4. = 4.) "evaluate just var";
  unit_test (evaluate (parse "x+3") 2. = 5.) "evaluate sum left";
  unit_test (evaluate (parse "4+x") 1. = 5.) "evaluate sum right";
  unit_test (evaluate (parse "x*3") 2. = 6.) "evaluate mult left";
  unit_test (evaluate (parse "4*x") 3. = 12.) "evaluate mult right";
  unit_test (evaluate (parse "x/3") 12. = 4.) "evaluate div left";
  unit_test (evaluate (parse "4/x") 2. = 2.) "evaluate div right";
  unit_test (evaluate (parse "x-3") 12. = 9.) "evaluate subtract left";
  unit_test (evaluate (parse "4-x") 10. = (-.6.)) "evaluate subtract right";
  unit_test (evaluate (parse "x^4") 2. = 16.) "evaluate pow left";
  unit_test (evaluate (parse "19^x") 1. = 19.) "evaluate pow right";
  unit_test (evaluate (parse "sin x") 0. = 0.) "evaluate sin";
  unit_test (evaluate (parse "cos x") 0. = 1.) "evaluate cos";
  unit_test_within 0.0001 (evaluate (parse "ln x") 10.) 2.3026 "evaluate ln";
  unit_test (evaluate (parse "~ x") 4. = (-.4.)) "evaluate neg";
  unit_test (evaluate (parse "15+(3+x)") 2. = 20.)
    "evaluate binop nested in binop";
  unit_test (evaluate (parse "15+(~x)") 2. = 13.)
    "evaluate unop nested in binop";
  unit_test (evaluate (parse "~(sin x)") 0. = 0.)
    "evaluate unop nested in unop";
  unit_test (evaluate (parse "~(x+14)") 4. = (-.18.))
    "evaluate binop nested in unop";
  unit_test (evaluate (parse "2") 5. = 2.) "evaluate number";
  unit_test (evaluate (parse "3+4") 5. = 7.) "evaluate sum only numbers";
  unit_test (evaluate (parse "4*51") 5. = 204.)
    "evaluate mult only numbers";
  unit_test_within 0.0001 (evaluate (parse "4/3") 1.) 1.3333
    "evaluate div only numbers";
  unit_test (evaluate (parse "17-3") 2. = 14.)
    "evaluate subtract only numbers";
  unit_test (evaluate (parse "2^4") 3. = 16.)
    "evaluate pow only numbers";
  unit_test (evaluate (parse "sin 0") 3. = 0.)
    "evaluate sin";
  unit_test (evaluate (parse "cos 0") 3. = 1.)
    "evaluate only numbers";
  unit_test_within 0.0001 (evaluate (parse "ln 10") 2.) 2.3026
    "evaluate ln only numbers";
  unit_test (evaluate (parse "~ 17") 4. = (-. 17.))
    "evaluate neg only numbers";;

let derivative_test () =
  unit_test (derivative (parse "x") = Num 1.) "derivative x";
  unit_test (derivative (parse "4") = Num 0.) "derivative 4";
  unit_test (evaluate (derivative (parse "4*3+21")) 2. = 0.)
    "derivative 4*3+21";
  unit_test (derivative (parse "4") = Num 0.) "derivative just number";
  unit_test (evaluate (derivative (parse "sin x")) 0. = 1.)
    "derivative sin x";
  unit_test_within 0.0001 (evaluate (derivative (parse "cos x")) 1.)
    (-.0.8415) "derivative cos x";
  unit_test (evaluate (derivative (parse "ln x")) 2. = 0.5) "derivative ln";
  unit_test (evaluate (derivative (parse "ln (x/5)")) 2. = 0.5)
    "derivative ln (x/5)";
  unit_test (evaluate (derivative (parse "~ x")) 5. = (-.1.)) "derivative neg";
  unit_test (evaluate (derivative (parse "~ (((3*x)*(8*x))^4)")) 5. =
    (-.207360000000.0)) "derivative ~ (((3*x)*(8*x))^4)";
  unit_test (evaluate (derivative (parse "x+x")) 4. = 2.)
    "derivative x+x";
  unit_test (evaluate (derivative (parse "5*x-x")) 13. = 4.)
    "derivative 5*x-x";
  unit_test (evaluate (derivative (parse "4*x^3")) 2. = 48.)
    "derivative 4*x^3";
  unit_test (evaluate (derivative (parse "((x-4)+(5-x))^3")) 2. = 0.)
    "derivative ((x-4)+(5-x))^3";
  unit_test (evaluate (derivative (parse "(x^3+x)^3")) 2. = 3900.)
    "derivative (x^3+x)^3";
  unit_test (evaluate (derivative (parse "9*x^4+3*x^3+x^2+x-15")) 2. = 329.) 
    "derivative 9*x^4+3*x^3+x^2+x-15";
  unit_test_within 0.0001
    (evaluate (derivative (parse "(4-x)/(x^3)")) 3.) (-.0.0741)
    "derivative (4-x)/(x^3)";
  unit_test_within 0.0001
    (evaluate (derivative (parse "(3*x)^(x^2)")) 2.) 11880.4811
    "derivative (3*x)^(x^2)";
  unit_test_within 0.0001
    (evaluate (derivative (parse "(sinx)^4+5*x-14")) 2.) 3.7485
    "derivative ((sinx)^4+5*x-14)";;

let find_zero_test () = 
  unit_test_within 0.0001
    (Option.get(find_zero (parse "3 * x - 1") 0. 0.0001 100)) 0.3333
    "find_zero 3x-1 0. 0.0001 100";
  unit_test_within 0.0001
    (Option.get(find_zero (parse "x-4") 3. 0.0001 10000)) 4.0000
    "find_zero x-4 3. 0.0001 10000";
  unit_test (find_zero (parse "x^3") 10. 0.0001 2 = None)
    "find_zero x^3 10. 0.0001 2";
  unit_test (find_zero (parse "51*x+x^3") 0. 0.0001 100 = Some 0.)
    "find_zero 51*x+x^3 0. 0.0001 100";
  unit_test (find_zero (parse "2*x-4") 4. 0.0001 2 = Some 2.)
    "find_zero 2*x-4 4. 0.0001 2";
  unit_test (find_zero (parse "2*x-4") 4. 0.0001 1 = None)
    "find_zero 2*x-4 4. 0.0001 1";
  unit_test (find_zero (parse "(x^3+x)^3-0.1") 4. 0.0001 3 = None)
    "find_zero (x^3+x)^3-0.1 4. 0.0001 3";
  unit_test (find_zero (parse "(x^3+x)^3-0.1") 4. 0.0001 17 = None)
    "find_zero (x^3+x)^3-0.1 4. 0.0001 17";
  unit_test_within 0.0001
    (Option.get(find_zero (parse "(x^3+x)^3-0.1") 4. 0.0001 18)) 0.4001
    "find_zero (x^3+x)^3-0.1 4. 0.0001 18";
  unit_test_within 0.0001
    (Option.get(find_zero (parse "(x^3+x)^3-0.1") 4. 0.0001 100)) 0.4001
    "find_zero (x^3+x)^3-0.1 4. 0.0001 100";
  unit_test (find_zero (parse "9*x^4+3*x^3+x^2+x-15") 2. 0.001 1 = None)
    "find_zero 9*x^4+3*x^3+x^2+x-15 2. 0.001 1";
  unit_test (find_zero (parse "9*x^4+3*x^3+x^2+x-15") 2. 0.001 5 = None)
    "find_zero 9*x^4+3*x^3+x^2+x-15 2. 0.001 5";
  unit_test_within 0.001
    (Option.get(find_zero (parse "9*x^4+3*x^3+x^2+x-15") 2. 0.001 6)) 1.0203
    "find_zero 9*x^4+3*x^3+x^2+x-15 2. 0.001 6";
  unit_test_within 0.001
    (Option.get(find_zero (parse "9*x^4+3*x^3+x^2+x-15") 2. 0.001 10)) 1.0203
    "find_zero 9*x^4+3*x^3+x^2+x-15 2. 0.001 10";
  unit_test (find_zero (parse "x^(1/3)") 0. 0.0001 100 = Some 0.)
    "find_zero x^(1/3) 0. 0.0001 100";
  unit_test (find_zero (parse "x^3") 0. 0.0001 2 = Some 0.)
    "find_zero x^3 0. 0.0001 2";
  unit_test_within 0.0001
    (Option.get(find_zero (parse "2-x^(1/2)") 3.9 0.0001 1000)) 4.0
    "find_zero 2-x^(1/2) 3.9 0.0001 1000";
  let mult_zeroes1 = Option.get(find_zero (parse "x^2-4") 0.5 0.0001 1000) in
  unit_test ((abs_float (mult_zeroes1 -. 2.) <= 0.0001) ||
             (abs_float (mult_zeroes1 +. 2.) <= 0.0001))
    "find_zero x^2-4 0.5 0.0001 1000";
  let mult_zeroes2 = Option.get(find_zero (parse "x^2-4") (-.0.5) 0.0001 1000)
  in
  unit_test ((abs_float (mult_zeroes2 -. 2.) <= 0.0001) ||
             (abs_float (mult_zeroes2 +. 2.) <= 0.0001))
    "find_zero x^2-4 (-.0.5) 0.0001 1000";;


let test_all () =
  contains_var_test () ;
  evaluate_test () ;
  derivative_test () ;
  find_zero_test () ;;


let _ = test_all () ;;