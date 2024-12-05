student_data = {"id1" : 
 {'name': ["ALI"],
  'class' : ['V'],  
 'subject_integration' : ['english,math,science']
},
'id2':
 {'name': ["BABAR"],
  'class' : ['V'],  
 'subject_integration' : ['english,math,science']
},
'id3':
 {'name': ["MUHAMMAD"],
  'class' : ['V'],  
 'subject_integration' : ['english,math,science']
},
'id4':
 {'name': ["ABDULLAH"],
  'class' : ['V'],  
 'subject_integration' : ['english,math,science']
},
}
result = {}
for key,value in student_data.items():
    if value not in result.values():
        result[key] = value
print(result)