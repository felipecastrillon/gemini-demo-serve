import functions_framework
from functions import *


@functions_framework.http
def main(request) -> dict:
    print("test event")
    output = results()
    return output
