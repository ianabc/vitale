The Vitale Property

 http://www.blog.republicofmath.com/the-number-3608528850368400786036725/


3608528850368400786036725 is the only 25 digit number which satisfies
the polydivisibilty (or Vitale) property. It is divisible by 25, it's
first 24 digits are divisible by 24, it's first 23 digits are divisible
by 23 etc. all the way down to 2. There are NO 26 digit numbers which
extend this property.

vitale.py: A python implementation which recursivly calculates these
numbers until a zero is found. It plots the number of vitale numbers for
each n if matplotlib is available. We use the arbitrary precision of
python integers.

vitale-numpy.py: Placeholder for a numpy version of vitale.py. Since we
know a-posteriori that 25 is the maximum number of digits we'll
encounter int28 or uint128 will comfortably handle all cases,
unfortunately these only seem to be in the development versions of numpy
at the moment.
