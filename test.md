```
items = {'tooth brush': 3.99, 'soda': 101.99}
for item, v in items.items():
  formatted_v = f"{round(v,2)}"
  print(f"{item}:{'.'*(40 - len(item) - len(formatted_v))}${formatted_v}")
```