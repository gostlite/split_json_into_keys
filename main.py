with open("./example_2_1.json") as f:
  data = json.load(f)
  num = 0
  for i, x in data.items():
    with open(f"./{str(num)}.json", 'w') as f_out:
      json.dump({i:x}, f_out)
    num +=1
