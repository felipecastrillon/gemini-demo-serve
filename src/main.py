import functions_framework
from functions import *


@functions_framework.cloud_event
def main(cloud_event):
    print("test event")
