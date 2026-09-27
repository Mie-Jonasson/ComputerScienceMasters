-- Types
type Image = Tensor Real [28, 28]
type Label = Index 10

-- (Additional) Parameters
@parameter -- epsilon ball size
epsilon : Real

@parameter(infer=True) -- size of training dataset
n : Nat

-- Dataset
@dataset
trainingImages : Vector Image n

@dataset
trainingLabels : Vector Label n

-- Network
@network
classifier : Image -> Tensor Real [10]

-- Util Functions
validImage : Image -> Bool -- are all pixels between 0 and 1
validImage x = forall i j . 0 <= x ! i ! j <= 1

advises : Image -> Label -> Bool -- Given image and Label, is the label correct given the network?
advises x i = forall j . j != i => classifier x ! i > classifier x ! j

boundedByEpsilon : Image -> Bool -- L_inf Norm, ensure all elements are bounded by epsilon
boundedByEpsilon x = forall i j . -epsilon <= x ! i ! j <= epsilon

robustAround : Image -> Label -> Bool
robustAround image label = forall perturbation .
  let perturbedImage = image - perturbation in
  boundedByEpsilon perturbation and validImage perturbedImage =>
    advises perturbedImage label

-- We then say that the network is robust for this data set if it is robust around
-- -- every pair of input images and output labels
@property
robust : Vector Bool n
robust = foreach i . robustAround (trainingImages ! i) (trainingLabels ! i)

