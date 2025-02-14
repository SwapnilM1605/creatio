import json
import logging

import requests
import azure.functions as func

# Microsoft Fabric OneLake Storage Location
ONELAKE_URL="https://onelake.dfs.fabric.microsoft.com/Analytics/CreatioData.Lakehouse/Files/"

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Received request from Creatio CRM.")

    try:
        # Read the request data
        data = req.get_json()
        file_name = f"contact_{data['Id']}.json"

        # Upload data to Microsoft Fabric OneLake
        response = requests.put(
            ONELAKE_URL + file_name,
            headers={"Authorization": "Bearer YOUR_ACCESS_TOKEN"},
            json=data
        )

        if response.status_code == 201:
            return func.HttpResponse("Data stored successfully in OneLake", status_code=200)
        else:
            return func.HttpResponse("Error storing data", status_code=500)

    except Exception as e:
        logging.error(str(e))
        return func.HttpResponse("Error processing request", status_code=500)
