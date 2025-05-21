#1 = collude 
#0 = defect

def play(roundNr,ownPrevMoves,otherPrevMoves,totalRounds):
    otherPrevMoves.sort()
    if len(otherPrevMoves) == 0:
        return 0
    return sum(otherPrevMoves) / len(otherPrevMoves) > 0.5
    return otherPrevMoves[len(otherPrevMoves)//2] 

  
def name():
  return 'tatfortit'