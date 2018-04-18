open util/ordering [Time]as T
open util/ordering[Coor] as C

--ordered 
sig Time {}
sig Coor {}
-- Position models the individual positions in the g
sig Pos {
  x: Coor,
  y: Coor
}

abstract sig Direction {} --The 4 cardinal directions 
one sig North,South,West,East extends Direction {}

some sig Robot {
--Direction rover is facing at any one time 
dir : Direction one -> Time,

--Rovers position at any one time 
pos : Pos one -> Time,

--Rover on/off status at any one time 
on: set Time
}

-- Frame condition
-- All other robot stay on or off as they ware (no_on_Changes)
--No other robot changes direction (no_direction_changes )
--No robot changes position(no_position_changes)

pred turn_on[rov:Robot, t,t':Time] {
-- preconditions
-- robot is off 
   !is_on[rov,t']
-- postconditions 
-- robot is on
   is_on[rov,t]
-- frame condition 
-- All other robot stay on or off as they were 
   no_on_changes[Robot - rov, t, t']
-- No other robot changes direction 
   //no_direction_changes[Robot, t, t']
-- No robot changes position
   //no_position_changes[
}


pred is_on[r:Robot,t:Time] {
t in r.on
}

pred no_on_changes[R: set Robot, t, t':Time] {
all r : R |t' in r.on iff t in r.on
}

pred no_position_changes[R:set Robot,t,t':Time]{
	all r:R | r.pos.t' = r.pos.t
}

pred no_direction_changes[R:set Robot,t,t':Time] {
	all r:R | r.dir.t' = r.dir.t
}


pred turn_off [rov:Robot,t,t':Time]
{
	is_on[rov,t]
	!is_on[rov,t']
	no_on_changes[Robot - rov, t, t']
	no_direction_changes[Robot,t,t']
	no_position_changes[Robot,t,t']
}
/*
pred turn_right[rov:Robot,t,t':Time]
{}
*/
pred turn_left[rov:Robot,t,t':Time]
{

	//precondition
	is_on[rov,t]
	//post condition --dir changes
	let d =  rov.dir.t | 
	let d' = ((d = North) => West else
				(d = West)=> South else
				(d = South)=> East else
				North) |
rov.dir.t' = d'	
//conditions
	--no_on_changes[Robot - rov, t, t']
	no_direction_changes[Robot,t,t']
	--no_position_changes[Robot,t,t']
}
pred turn_right[rov:Robot,t,t':Time]
{
	is_on[rov,t]

	let d = rov.dir.t |
	let d' = ((d = North) => East else
				(d = East)=> South else
				(d = South)=> West else
				North) |
	rov.dir.t' = d'
	--no_on_changes[Robot - rov, t, t']
	no_direction_changes[Robot-rov,t,t']
	--no_position_changes[Robot-rov,t,t']
}

pred forward [rov: Robot, d: Direction, t,t': Time] {
   	is_on[rov, t]
   	let d = rov.dir.t | 
	let np = nxt_pos[rov.pos.t, d] | {
  		some np	
     	rov.pos.t' = np
	}
   	no_on_changes[Robot, t, t'] 
   	no_direction_changes[Robot, t, t']
   	no_position_changes[Robot - rov, t, t']
}
fun nxt_pos [p: Pos , d: Direction]: Pos{
  let p_north = { 
							s: Pos | s.x = p.x and s.y = C/next[p.y] } |
  let p_south = { 
							s: Pos | s.x = p.x and s.y = C/prev[p.y] } |
  let p_east = { 
							s: Pos | s.y = p.y and s.x = C/next[p.x] } |
  let p_west  = { 
							s: Pos | s.y = p.y and s.x = C/prev[p.x] } |
    (d = North) => p_north else
    (d = South) => p_south else
    (d = East)  => p_east else
                   p_west
}

pred transitions 
{
--possible trnsitions 
 all t:Time -T/last | let t' = T/next [t] |
   some r :Robot |
     turn_on [r,t,t'] or
     turn_off [r,t,t'] or
	 turn_left [r,t,t'] or
    turn_right [r,t,t'] or
     (some d:Direction | forward [r,d,t,t'])

 
}
 
one sig R1 extends Robot {}
one sig P0 extends Pos {}

-- P0 is the origin position of the coordinate system
fact {
 P0.x = C/first 
 P0.y = C/first
}

pred init [t: Time] {
   R1.pos.t = P0
   R1.dir.t = East
   !is_on[R1, t] 
   all r: Robot - R1 | R1.pos.t != r.pos.t
}
/*assert default{
one r:Robot | one dir:Direction |one t,t':Time | r.dir.t=r.dir.t'
}*/
assert checkd{ 
one d:Direction |one r:Robot 
 }

pred show(){}
run show
