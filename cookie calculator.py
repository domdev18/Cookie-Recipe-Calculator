cookies = 0.0000
#Initializing the soon to be inputed variable. Will hold the number of cookies that the user wants
print("How many cookies are needed?")
cookies=int(input())
sugar=2.5/63
butter=1.75/63
flour=3.75/63
#the above 3 variables are calculating the ingrediants need for one cookie
sugarneeded=round(cookies*sugar,3)
butterneeded=round(cookies*butter,3)
flourneeded=round(cookies*flour,3)
#the above 3 variables are calculating the number of cookies the user wants by the ingrediants needed for one cookie(rounded to 3 decimal places).
print("you will need ", sugarneeded," cups of sugar, ", butterneeded," cups of butter, ",flourneeded,"cups of flour.")
