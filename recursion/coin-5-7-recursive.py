def change(amount):
  if amount == 24:
    return [5, 5, 7, 7];
  if amount == 25:
    return [5, 5, 5, 5, 5];
  if amount == 26:
    return [5, 7, 7, 7];
  if amount == 27:
    return [5, 5, 5, 5, 7];
  if amount == 28:
    return [7, 7, 7, 7];
  if amount > 28:
    coins = change (amount - 5);
    coins.append(5);  
  return coins

change(35);
change(36);
change(37);
change(38);
change(39);