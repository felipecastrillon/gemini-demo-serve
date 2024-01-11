import functions_framework
from functions import *


@functions_framework.http
def main(request):
    print("test event")
    results()
