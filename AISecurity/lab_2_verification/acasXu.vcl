-- Types
type Input = Tensor Real [5]
type Output = Tensor Real [5]
type UnnormalisedInput = Input

-- Constants & Index Maps
pi = 3.141592

distanceToIntruder = 0   -- measured in feet
angleToIntruder    = 1   -- measured in radians
intruderHeading    = 2   -- measured in radians
speed              = 3   -- measured in feet/second
intruderSpeed      = 4   -- measured in feet/second

clearOfConflict = 0
weakLeft        = 1
weakRight       = 2
strongLeft      = 3
strongRight     = 4

-- The Network
@network
acasXu : Input -> Output

-- Normalizing (Preprocessing) Problem Space -> Input Space
minimumInputValues : UnnormalisedInput
minimumInputValues = [0, -pi, -pi, 0, 0]

maximumInputValues : UnnormalisedInput
maximumInputValues = [60261, pi, pi, 1200, 1200]

meanScalingValues : UnnormalisedInput
meanScalingValues = [19791.091, 0.0, 0.0, 650.0, 600.0]

normalise : UnnormalisedInput -> Input
normalise x = foreach i .
  (x ! i - meanScalingValues ! i)
    / (maximumInputValues ! i - minimumInputValues ! i)

-- Network of Normalized Problem Space Vectors
normAcasXu : UnnormalisedInput -> Output
normAcasXu x = acasXu (normalise x)

-- Defining Utility Functions
validInput : UnnormalisedInput -> Bool
validInput x = forall i .
  minimumInputValues ! i <= x ! i <= maximumInputValues ! i

minimalScore : Index 5 -> UnnormalisedInput -> Bool
minimalScore i x = forall j .
  i != j => normAcasXu x ! i < normAcasXu x ! j

directlyAhead : UnnormalisedInput -> Bool
directlyAhead x =
  1500  <= x ! distanceToIntruder <= 1800 and
  -0.06 <= x ! angleToIntruder    <= 0.06

movingTowards : UnnormalisedInput -> Bool
movingTowards x =
  x ! intruderHeading >= 3.10  and
  x ! speed           >= 980   and
  x ! intruderSpeed   >= 960

-- Defining the property to test
@property
property3 : Bool
property3 = forall x .
  validInput x and directlyAhead x and movingTowards x =>
  not (minimalScore clearOfConflict x)

