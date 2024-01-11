import firebase_admin
from firebase_admin import firestore


def results():
    # app = firebase_admin.initialize_app()
    db = firestore.client()

    # users_ref = db.collection("users")
    # docs = users_ref.stream()
    cities_ref = db.collection("gemini-demo-images")
    query = cities_ref.order_by(
        "timeStamp", direction=firestore.Query.DESCENDING).limit(3)
    results = query.stream()

    for doc in results:
        print(f"{doc.id} => {doc.to_dict()}")

    return results
