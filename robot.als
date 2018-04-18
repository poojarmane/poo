open util/ordering[Time] as T
open util/ordering[Coor] as C

--Co-ordinets Stritly
sig Time {}
sig Coor {}

sig Position {x: Coor, y:Coor}

--Th e Cordinal direction 
abstract sig Direction {}

one sig North,South,East,West extends Direction {}

some sig Robot {
-- Direction rover is facing at any one time
dir: Direction one ->Time ,

--Rover's position at any one time
pos: Position one -> Time,

--Rover's on/off status at any one time 
on:set Time
}

--operators
--Turn on
--TurnOff
--Turn left
--Turn rigth

pred turn_on [rov: Robot ,t,t':Time]{
-- Pre Condition
--Robot is OFF at time t (!is_on)
!is_on[rov,t]
--Robot is on
is_on[rov,t']
no_on_changes[Robot - rov, t,t']
no_direction_changes[Robot ,t,t']
no_position_changes[Robot, t,t']
}
pred is_on[r:Robot,t:Time]{
t in r.on
}





pred turn_off[rov:Robot,t,t':Time]
{ 
  is_on[rov,t]--time is on  precondition
 !is_on[rov,t'] //postcondition
no_on_changes[rov-Robot,t,t']
no_direction_changes[Robot,t,t']
no_position_changes[Robot,t,t']
}


pred  turn_right[rov:Robot,t,t':Time]
{
    is_on[rov,t]	
 //post condition
--direction changes
  let d=rov.dir.t | 
  let d'=(d=North) =>East else 
           (d=East) =>South else
           (d=South) =>West else  North  |
   rov.dir.t'=d'
  //conditions
  no_on_changes[Robot,t,t']
no_direction_changes[Robot-rov,t,t']
no_position_changes[Robot,t,t']
}

pred turn_left[rov:Robot,t,t':Time]
{
 //precondition
   is_on[rov,t]	
 //post condition
--direction changes
  let d=rov.dir.t | 
  let d'=(d=North) =>West else 
           (d=West) =>South else
           (d=South) =>East else  North  |
   rov.dir.t'=d'
  //conditions
  no_on_changes[Robot,t,t']
no_direction_changes[Robot-rov,t,t']
no_position_changes[Robot,t,t']

}
pred move_forword[rov:Robot,t,t':Time]
{
is_on[rov,t]
rov.dir.t=d
let newposition=next_pos[rov.pos.t,d]|{
some newposition
rov.pos.t'=newposition
}
no_on_changes[Robot,t,t']
no_direction_changes[Robot,t,t']
no_position_changes[Robot -rov,t,t']
}
pred is_on[r:Robot,t:Time]
{
t in r.on
}
pred no_on_changes[R:set Robot,t,t':Time]{
all r: R|
t' in r.on iff t in r.on
}
pred no_direction_changes[R:set Robot,t,t':Time]{
all r:R|
r.dir.t'=r.dir.t
}
fun next_pos[p:Position,d:Direction]:Position{
let pos_north_of_p={q:Position | q.x=p.x and q.y=C/next[p.y]}|
let pos_south_of_p={q:Position |q.x=p.x and q.y=C/prev[p.y]}|
let pos_east_of_p={q:Position|q.y=p.y and q.x=C/next[p.x]}|
let pos_west_of_p={q:Position|q.y=p.y and q.x=C/prev[p.x]}|
(d=North)=>pos_north_of__p else
(d=Soth)=>pos_south_of_p else
(d=East)=>pos_east_of_p else
(d=west)=>pos_west_of_p 
}
pred transitions {
  all t: Time - T/last | let t' = T/next[t] | 
    some r: Robot |
      turn_on [r, t, t'] or
      turn_off [r, t, t'] or
      turn_left [r, t, t'] or
      turn_right [r, t, t'] or
      (some d: Direction | move_forword [r, d, t, t'])
}
--one sig R1 extends Rover {}
--one sig P0 extends Position {}


run turn_off for 5 but exactly 2 Robot

run turn_right
run turn_left
run turn_off

--pred run for 3 
--run  {}
run turn_on 
//run move_forword

