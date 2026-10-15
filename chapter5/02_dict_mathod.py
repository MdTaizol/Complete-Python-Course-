marks = {
    "Taizol" : 100,
    "Rabbi" : 56,
    "Rohan" : 23,
    0: "Taizol"
}
# print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Taizol":99})
print(marks)
# print(marks.get("Harray"))#print none
# print(marks.get["Taizol"]) #print error.
# print(marks.pop("Rabbi"))
print(marks.popitem())
print(marks)
