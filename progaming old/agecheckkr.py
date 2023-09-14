'''ey doe dan'''
def agectel(age):
    if age > 18:
        return "ja"
    if age > 13:
        return "nee"
    return "Terug naar basis school"

age = int(input("ben je oud?"))
print(agectel(age))