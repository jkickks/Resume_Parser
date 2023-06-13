import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

# Ask User For Keywords to look for
num_inputs = int(input("How many different keywords are you looking for in the resume? "))
user_inputs = []

for i in range(num_inputs):
    user_input = input("Enter input {}: ".format(i+1))
    user_inputs.append(user_input)

k = ' '.join(user_inputs)
keywords = k.split()


# Retrieve the parsed PDF from Firestore
doc_ref = db.collection('resumes').document('testing123')
doc = doc_ref.get()
text = doc.to_dict().get('text', '')

# Check for specific keywords
found_keywords = []
for keyword in keywords:
    if keyword.lower() in text.lower():
        found_keywords.append(keyword)



# Print the found keywords
if found_keywords:
    print('Found keywords:', found_keywords)
    
else:
    print('No keywords found.')

