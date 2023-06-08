welcome_prompt = "Welcome Doctor Wilson. What would you like to do today?\n - To list all patients, press 1\n - To run diagnosis, press 2\n - To quit, press q\n "
name_prompt = "What is the patient's name?\n"
appearance_prompt = "How is the parient's general appearance?\n - 1: Normal Appertance \n 2: Irritable or lethargic\n 3: Are they bleeding?\n"
eye_prompt = "How are the parient's eyes? \n 1: Eyes are normal or slightly sunken \n 2:Eyes very sunken\n"
skin_prompt = "How is the parient's skin when you pinch it?\n 1: Nomral skin pinch\n 2: Slow skin pinch\n"
error_message = "Could not save parient and diagnosis due to invalid input."
severe_dehydration = "Severe dehydration"
some_dehydration = "Some dehydration"
no_dehydration = "No dehydration"
blood_prompt = "How badly are they bleeding?\n 1:Alittle blood\n 2:Has a wound but is not bleeding\n"
patients_and_diagnoses = [
  "Briana - No dehydration",
  "Abril - Severe dehydration",
  "Carlos - Some dehydration"
]


def list_patients():
  for patient in patients_and_diagnoses:
    print(patient)

def start_new_diagnosis():
  name = input(name_prompt)
  diagnosis = assess_appearance()
  save_new_diagnosis(name, diagnosis)

def save_new_diagnosis(name, diagnosis):
  if name == "" or diagnosis == "":
    print(error_message)
    return
  final_diagnosis = name + "-" + diagnosis
  patients_and_diagnoses.append(final_diagnosis)
  print("Final Diagnosis:", final_diagnosis, "\n" )
  
def assess_appearance():
  appearance = input(appearance_prompt)
  if appearance == "1":
    eyes = input(eye_prompt)
    return assess_eyes(eyes)
  elif appearance == "2":
    skin = input(skin_prompt)
    return assess_skin(skin)
  elif appearance == "3":
    blood = input(blood_prompt)
    return assess_blood(blood)
  else: 
    return ""

def assess_skin(skin):
  if skin == "1":
    return some_dehydration
  elif skin == "2":
    return severe_dehydration
  else:
    return ""

def assess_eyes(eyes):
  if eyes == "1":
    return no_dehydration
  elif eyes == "2":
    return severe_dehydration
  else:
    return ""
def assess_blood(blood):
  if blood == "1":
    return no_dehydration
  elif blood == "2":
    return severe_dehydration
  else:
    return ""
def main():
  while (True):
    selection = input(welcome_prompt)
    if selection == "1":
      list_patients()
    elif selection == "2":
      start_new_diagnosis()
    elif selection == "q":
      return


main()
