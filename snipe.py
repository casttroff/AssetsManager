import requests
from io import StringIO
import json

def get_assets(serial_number):
        url = "https://mercadoenvio.snipe-it.io/api/v1/hardware/bytag/" + serial_number
        headers = {
            'authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjQ1ZDZmODVmN2U5Y2U4YmVkZTIzNTU4MTQ5ZWI4ZmUwODg3NTczZWEzMmZiZjFiMWUxMWRhMzdiNjE5NDdkNzM5YzIwMTBiZDlkMWU2NTM3In0.eyJhdWQiOiIxIiwianRpIjoiNDVkNmY4NWY3ZTljZThiZWRlMjM1NTgxNDllYjhmZTA4ODc1NzNlYTMyZmJmMWIxZTExZGEzN2I2MTk0N2Q3MzljMjAxMGJkOWQxZTY1MzciLCJpYXQiOjE1ODkyNzMyODAsIm5iZiI6MTU4OTI3MzI4MCwiZXhwIjoxNjIwODA5MjgwLCJzdWIiOiIyIiwic2NvcGVzIjpbXX0.KqL6QfN6olnzFVE3QnCerkQWX6KFzdMxiJS2VmWcoPjovdVPorfluQ5gkWvDSCUL4VINk8O7eXdwv4w4ORa91AfI4Yx61NvPpvUfiDYKOUo9o4GhOmHv59qus1cFZ_nR9HYz0xZ6GTltYEQs0DgFGFfz63kTy8-CspIUWH-sZtPr8s8vleq1TvAm-OxlStSOCUWb1LK4aubLkZbPeO_1xkcU10KdT1gz3gr8lx8ANScG2DQ3N8TjtT2-LK210ePtvEGsNoq-vC2yRYEJmeFlxQ_Ou4O1azfZcuk_2oc0rwMbCf62cpTT3d8yOBb6AEubyTxpdyDpKmqhww5AOhEqkoXZo7aIijnvVr403BlDLlfxPPHZ7zUgliUbEXCjUtRSBcVSby5YaTbWhnSLJDuimafR2FUW8L9ySzfUXjjE9OKGrUIxFx0-mDUvPu__Vi_oLOErVTZ7gn0KQT4gqCzbMtUz7QUpq7mh0tWSboX4-81xn1Cyvk1xkS65oKtpULpv56jw8DIXHokCUIQEP5W-2v6q-vWABMl_04GfC4UEJfcWeLZHV2n7pGXBS-hKulG-jL-vLZ9Mk0-V5PWJ8fNwlDnaiC14M6Ok7oUPbkgYC8G0w5CSVVvfrDevXW8SbvOcEyLoFDsIbUQfmmGqgfqrz4OrsYT3u5QJ-EOc9t-WO-o",
            'accept': "application/json",
            'content-type': "application/json"
            }
        response = requests.request("GET", url, headers=headers)
        data = response.json()
        print(data)
        for key,value in data.items():
                if key == "model":
                        model = value['name']
                if key == "manufacturer":
                        manufacturer = value['name']
                if key == "custom_fields":
                        mac = value['MAC Address']['value']

        print('Model: {} Manufacturer: {} MAC: {}'.format(str(model), str(manufacturer), str(mac)))
        return (model,manufacturer,mac)

#if __name__ == '__main__':
#    get_assets('eslaprueba')
