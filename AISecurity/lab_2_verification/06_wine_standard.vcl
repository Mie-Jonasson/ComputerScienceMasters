
type Features = Tensor Real [11]
type Score = Tensor Real [8]

@network
classifier : Features -> Score

validInput : Features -> Bool
validInput x = forall i . 0 <= x ! i <= 1

@parameter
epsilon : Real

@parameter
delta : Real

closeInputs : Features -> Features -> Bool -- inputs are within epsilon of each other
closeInputs x y = forall i . -epsilon <= x ! i - y ! i <= epsilon

closeOutputs : Score -> Score -> Bool -- outputs are within delta of each other
closeOutputs a b = forall i . -delta <= a ! i - b ! i <= delta

-- for all inputs x, if x is within epsilon of y, then the output of the model is within delta of the output of the model at y
standardRobustAround : Features -> Score -> Bool
standardRobustAround y fy = forall x .
  validInput x and closeInputs x y =>
    closeOutputs (classifier x) fy

@parameter(infer=True)
n : Nat

@dataset
trainingInputs : Vector Features n

@dataset
trainingScores : Vector Score n

@property
standardRobust : Vector Bool n
standardRobust = foreach i .
  standardRobustAround (trainingInputs ! i) (trainingScores ! i)
