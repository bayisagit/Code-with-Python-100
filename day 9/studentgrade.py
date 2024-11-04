studentgrade={
    "harry":81,
    "hermione":78,
    "ron":99,
    "draco":74,
    "neville":62,
}
for k in studentgrade:
    score=studentgrade[k]
    if score>90:
        studentgrade[k]="outstanding"
    elif score>80:
        studentgrade[k]="exceeds expectations"
    elif score>70:
        studentgrade[k]="acceptable"
    else:
        studentgrade[k]="FAIL"
print(studentgrade)