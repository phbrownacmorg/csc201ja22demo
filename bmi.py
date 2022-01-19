from typing import List, Tuple

# Test cases:
# Pete Davidson: 6'1" (73 in.), 183 lbs. (https://celebrityinside.com/body-measurements/actor/pete-davidson-height-weight-age-facts-family-wiki/)
# Ariana Grande: 5'0.5" (60.5 in.), 108 lbs. (https://healthyceleb.com/ariana-grande/)
# Taylor Swift: 5'9.25" (69.25"), 139 lbs. (https://celebhealthmagazine.com/taylor-swift-measurements-size/)
# Steve Jobs: 6'2" (74"), 154 lbs. (https://healthyceleb.com/steve-jobs/)
# Derrick Lewis: 6'3" (75"), 265 lbs. (https://en.wikipedia.org/wiki/Derrick_Lewis)
# Hasan Minhaj: 5'11.5" (71.5"), 165 lbs. (https://celebrityinside.com/body-measurements/media/hasan-minhaj-height-weight-shoe-size-facts-family/)
# Ryan Reynolds: 6'2" (74"), 190 lbs. (https://blog.kinobody.com/best-of/celebrity-workout-routines/ryan-reynolds-height-weight/)
# Naomi Campbell: 5/9" (69"), 128 lbs. (https://celebritytall.com/naomi-campbell/)
# Jack Black: 5'6" (66"), 245 lbs. (https://healthyceleb.com/jack-black/)
# Rachel Zoe: 5'8" (68"), 121 lbs. (https://bodysize.org/en/rachel-zoe/)

def getHeightWeight() -> Tuple[float, float]:
    # Get weight and height from the user and return them as a tuple.
    # Weight and height are in pounds and inches, respectively.
    height:float = float(input('Please enter a height in inches: '))
    weight:float = float(input('Please enter a weight in pounds: '))
    return height, weight

def calcBMI(height:float, weight:float) -> float:
    # Calculate the BMI, given the height and weight in inches and pounds.
    # Formula from https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html
    return (weight / height**2) * 703

def bmiClass(bmi:float) -> str:
    # Given a numeric BMI, find the classification into which it falls
    result:str = '' # Give result a bogus value, which will shortly be changed

    # Note the classes are in strictly increasing order.  This allows me
    # not to have to test the bottom end of each range *in addition to* the top end,
    # because anything below the bottom of each range will have been identified already.
    # The same trick could be used in strictly decreasing order, but would break if I
    # mixed up the order.
    if bmi < 18.5:
        result = 'underweight'
    elif bmi < 25: # >= 18.5 implied, because those cases already got processed
        result = 'healthy weight'
    elif bmi < 30: # >= 25 implied, because those cases already got processed
        result = 'overweight'
    else: # No upper bound on the range
        result = 'obese'
    return result

def main(args:List[str]) -> int:
    # Get weight and height
    height, weight = getHeightWeight() # type: float, float
    bmi:float = calcBMI(height, weight)
    print('Height: {0:.0f}"\t\tWeight: {1:.0f} lbs.\tBMI: {2:.1f}'.format(height, weight, bmi))
    print('This person is classed as', bmiClass(bmi))

    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)