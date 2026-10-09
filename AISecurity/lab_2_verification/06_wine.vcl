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

alcohol = 10

highQuality : Features -> Bool
highQuality x = advises x 5 or advises x 6 or advises x 7

equals : Features -> Features -> Bool
equals x y = forall k . x ! k == y ! k

highAlcoholAround : Features -> Bool
highAlcoholAround x = forall y .
  validInput y and equals y x and y ! alcohol >= 0.3 => -- 0.3 ~10.??% after scaling
    highQuality y

@property
robust : Vector Bool n
robust = foreach i . robustAround (trainingInputs ! i) (trainingLabels ! i)

@property
highAlcoholIsGood : Vector Bool n
highAlcoholIsGood = foreach i . highAlcoholAround (trainingInputs ! i)
