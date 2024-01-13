#Escape character
#
#\n -line breake
#\s =[\n \t \r \v \f

print("line \nbreak")
#\v
print("line \v break")

#\t -tab
print("it \thelp  tab")

#\b -backspace
print("thi is for \bbackspace")

#\r -carriage return- it escape according to the  character 
print("this  is \rnothing")

#\f = form 
print("page \f page")

#
print("hello \ name")

#remove white space 
import re
replace_name="this is    python  \n course"
result=re.sub('\s+',' ',replace_name) #\s remove all escape character
print(result)

