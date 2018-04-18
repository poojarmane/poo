

sig WaterAtm{
  
   Coin:set insertcoin,
   liters:set capacity,
 
}


abstract sig insertcoin{}
sig onecoin extends insertcoin{}
sig fivecoin extends insertcoin{}
sig tencoin extends insertcoin{}

abstract sig capacity{}
sig onelit extends capacity{}
sig twolit extends capacity{}
sig fivelit extends capacity{}
 

pred coins{

one w: WaterAtm| all f:fivecoin|f in  w.Coin 
one w: WaterAtm|all o:onecoin|o in w.Coin
one w:WaterAtm|all t:tencoin|t in w.Coin
}
run coins
pred checkCoin{
all o:onecoin|one ol:onelit|one w:WaterAtm|ol in w.Coin
all f:fivecoin|one tw:twolit|one w:WaterAtm|tw in w.Coin
all t:tencoin|one fv:fivelit|one w:WaterAtm|fv in w.Coin
}

sig user{
putcoin:WaterAtm
}

abstract sig water{}
one sig coolwater extends water{}
one sig normalwater extends water{}



