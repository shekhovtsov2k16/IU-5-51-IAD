import defs


ivan = {
    "name" : "ivan",
    "age" : 34,
    "children" : [{
        "name" : "vasya",
        "age" : 12,
    }, {
        "name" : "tolya",
        "age" : 10,
    }],
}

darina = {
    "name" : "darina",
    "age" : 41,
    "children" : [{
        "name" : "kirill",
        "age" : 21,
    }, {
        "name" : "pavel",
        "age" : 15,
    }],
}
emps = [ivan, darina]

filtered = defs.filter_emps(emps, 18)
print(filtered)