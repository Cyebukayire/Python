students = {
    "shalom": 1,
    "fadhili": 89,
    "peace":879,
    "tito": 2,
    "dorcas": 4
}

name = raw_input("Urashaka kurebera nde? ").lower()
umwanya = str(students.get(name))
if umwanya == "None":
    print("""
Egoko! Cika Feri shahhahahah 
uwo mwana ntaho 
tumuzi kwa Pastor
    """)
else:
    print("Ehhhh! Umwanya wa " + name +" ni " + umwanya)