d1={"b":1,"a":4,"c":3,}
d2={"e":7,"d":8,"f":9,}
print("dictionary 1:",d1)
print("dictionary 2:",d2)
sorted_dict=dict(sorted(d1.items()))
print("sorted_dictionary:",sorted_dict)
merged={**d1 , **d2}
print("merged dictionary:",merged)
s1={1,2,3,4}
s2={3,4,5,6}
print("set 1:",s1)
print("set 2:",s2)
print("number of elements in set 1:",len(s1))
print("common elements:",s1.intersection(s2))
print("unique elements:",s1.symmetric_difference(s2))
