import functions_framework
from functions import *


@functions_framework.http
def main(request):
    print("test event")
    output = results()
    print(output.values())
    return output.values()
