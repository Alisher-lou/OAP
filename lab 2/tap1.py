print("1-тапсырма. Айнымалылар және типтер")
full_name = input("Аты-жөніңізді енгізіңіз: ")                    
birth_year = int(input("Туған жылыңызды енгізіңіз: "))            
average_score = float(input("Орташа балыңызды енгізіңіз: "))      
is_excellent = average_score >= 90                               

print("Аты-жөні:", full_name, type(full_name))
print("Туған жылы:", birth_year, type(birth_year))
print("Орташа балы:", average_score, type(average_score))
print("Үздік студент:", is_excellent, type(is_excellent))
print()
