-- Types
type Features = Tensor Real [11]
type Label = Index 8

-- (Additional) Parameters
@parameter
epsilon : Real

@parameter(infer=True)
n : Nat

-- Dataset
@dataset
trainingInputs : Vector Features n

@dataset
trainingLabels : Vector Label n

-- Network
@network
classifier : Features -> Tensor Real [8]

-- Util Functions
validInput : Features -> Bool
validInput x = forall i . 0 <= x ! i <= 1

advises : Features -> Label -> Bool
advises x i = forall j . j != i => classifier x ! i > classifier x ! j

boundedByEpsilon : Features -> Bool
boundedByEpsilon x = forall i . -epsilon <= x ! i <= epsilon

robustAround : Features -> Label -> Bool
robustAround input label = forall perturbation .
  let perturbed = input - perturbation in
  boundedByEpsilon perturbation and validInput perturbed =>
    advises perturbed label

-- alcohol is the last normalised feature; 0.7 is a high ABV after min-max scaling.
-- labels 5, 6, 7 are quality scores 6, 7, 8
alcohol = 10

highQuality : Features -> Bool
highQuality x = advises x 5 or advises x 6 or advises x 7

@property
robust : Vector Bool n
robust = foreach i . robustAround (trainingInputs ! i) (trainingLabels ! i)

@property
highAlcoholIsGood : Bool
highAlcoholIsGood = forall x .
  validInput x and x ! alcohol >= 0.7 =>
    highQuality x
