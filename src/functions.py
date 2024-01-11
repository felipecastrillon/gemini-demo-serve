import firebase_admin
from firebase_admin import credentials, firestore


def results():
    # app = firebase_admin.initialize_app()
    # db = firestore.client()

    if not firebase_admin._apps:
        firebase_admin.initialize_app()

    # app_options = {'projectId': 'cf-data-analytics'}
    # default_app = firebase_admin.initialize_app(options=app_options)

    db = firestore.client()

    # users_ref = db.collection("users")
    # docs = users_ref.stream()
    cities_ref = db.collection("gemini-demo-images")
    query = cities_ref.order_by(
        "timeStamp", direction=firestore.Query.DESCENDING).limit(3)
    results = query.stream()

    outputArray = []
    results = {}

    for doc in results:
        outputArray.append(doc.to_dict())

    results["data"] = outputArray

    return results
