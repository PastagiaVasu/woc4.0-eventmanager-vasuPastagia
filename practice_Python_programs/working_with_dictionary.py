# basicaly used to store key value pair and it is same as hashmap
# we use {} barces to represent dictionary
# key should be always unique
monthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "Octomber",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversion["Apr"])
# print(monthConversion["Dce"]) will give and error
print(monthConversion.get("Jan"))
print(monthConversion.get("dce"),"Not a valid key")  #will not give any error it will just print none if data not found