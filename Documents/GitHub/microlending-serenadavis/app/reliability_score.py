def age_score(age):
  if age < 10:
    return 1
  elif age < 16:
    return 2
  elif age < 24:
    return 3
  elif age < 30:
    return 4
  else:
    return 5

def education_score(education):
  if education == 0:
    return 0
  elif education == 1:
    return 3
  elif education == 2:
    return 4
  else:
    return 5
