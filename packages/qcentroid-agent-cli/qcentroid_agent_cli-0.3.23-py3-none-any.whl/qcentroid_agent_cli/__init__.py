
import requests
import json
import os
import mimetypes
from qcentroid_agent_cli.model import Status, StatusEntity

import ssl

api_base_url = "https://api.qcentroid.xyz"

class QCentroidAgentClient:
    # Init class with base parameters
    def __init__(self, base_url=None, pat=None, job_name=None):
        self.base_url = api_base_url #default production url
        
        if base_url is not None:
            self.base_url = base_url
        else:
            self.base_url = os.environ.get('QCENTROID_PUBLIC_API', api_base_url)
        if pat is not None:             
            self.pat = pat
        else:
            self.pat = os.environ.get('QCENTROID_TOKEN')
        if job_name is not None:             
            self.name = job_name
        else:
            self.name = os.environ.get('EXECUTOR_ID')
            
    def getHeaders(self):
        return {
            "Authorization": f"Bearer {self.pat}",
            "Accept": "application/json",  # Set the content type based on your API's requirements
            "Content-Type": "application/json",  # Set the content type based on your API's requirements
        }

    #GET [core]/agent/job/{job_name}/data/input
    def obtainInputData(self) -> dict:        

        try:
            response = requests.get(f"{self.base_url}/agent/job/{self.name}/data/input", headers=self.getHeaders())

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse and use the response data as needed                
                data={}
                if 'Transfer-Encoding' in response.headers and response.headers['Transfer-Encoding'] == 'chunked':
                    datab=b""
                    for chunk in response.iter_content(chunk_size=1024):
                        datab += chunk                    
                    data = json.loads(datab)
                else:
                  data = response.json()
                print("API Response:", data)
                return data #return json 
            else:
                print(f"Error: {response.status_code} - {response.text}")
                response.raise_for_status()

        except requests.RequestException as e:
            print(f"Request failed: {e}")
            raise e            
        except Exception as e:
            # Handle any exceptions or errors here
            print(f"Unexpected Error: {e}")
            raise e

    #POST [core]/agent/job/{job_name}/data/output
    def sendOutputData(self, data:dict) -> bool:
        
        try:
            response = requests.post(f"{self.base_url}/agent/job/{self.name}/data/output", json=data, headers=self.getHeaders())
            
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse and use the response data as needed
                data = response.json()
                print("API Response:", data)
                return True
            else:
                print(f"Error: {response.status_code} - {response.text}")
                response.raise_for_status()

        except requests.RequestException as e:
            print(f"Request failed: {e}")
            raise e            
        except Exception as e:
            # Handle any exceptions or errors here
            print(f"Unexpected Error: {e}")
            raise e
        

    #POST /agent/job/{job_name}/data/output/additional
    def sendAdditionalOutputFile(self, filename:str) -> bool:
        try:
            with open(filename, "rb") as file:
                response = requests.post(f"{self.base_url}/agent/job/{self.name}/data/output/additional", headers=self.getHeaders(), files={"file": file})
                if response.status_code == 200:
                    # Parse and use the response data as needed
                    data = response.json()
                    print("API Response:", data)
                    return True
                else:
                    print(f"Error: {response.status_code} - {response.text}")
                    response.raise_for_status()

        except requests.RequestException as e:
            print(f"Request failed: {e}")
            raise e            
        except Exception as e:
            # Handle any exceptions or errors here
            print(f"Unexpected Error: {e}")
            raise e

    #GET [core]/agent/job/{job}/execution-log
    def sendExecutionLog(self, filename:str) -> bool:
        try:
           
            with open(filename, "rb") as file:
                response = requests.post(f"{self.base_url}/agent/job/{self.name}/execution-log", headers=self.getHeaders(), files={"file": file})
                if response.status_code == 200:
                    # Parse and use the response data as needed
                    data = response.json()
                    print("API Response:", data)
                    return True
                else:
                    print(f"Error: {response.status_code} - {response.text}")
                    response.raise_for_status()
                
            
        except FileNotFoundError as e:
            print(f"Error: {e}")
            raise e
        except ValueError as e:
            print(f"Error: {e}")
            raise e
        except Exception as e:
            # Handle any other unexpected exceptions here
            print(f"Unexpected Error: {e}")
            raise e        
    #GET [core]/agent/job/{job}/status
    def status(self) -> StatusEntity:
        try:
            response = requests.get(f"{self.base_url}/agent/job/{self.name}/status", headers=self.getHeaders())
            
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse and use the response data as needed
                data = response.json()
                print("API Response:", data)
                current_status = StatusEntity.from_dict(data)
                return current_status
            else:
                print(f"Error: {response.status_code} - {response.text}")
                
                response.raise_for_status()
        except FileNotFoundError as e:
            print(f"Error: {e}")
            raise e
        except ValueError as e:
            print(f"Error: {e}")
            raise e
        except Exception as e:
            # Handle any other unexpected exceptions here
            print(f"Unexpected Error: {e}")
            raise e

    #POST [core]/agent/job/{job}/status
    def status(self, data:StatusEntity) -> bool:
        try:
            response = requests.post(f"{self.base_url}/agent/job/{self.name}/status", headers=self.getHeaders(), json=data.to_dict())
            if response.status_code == 200:
                # Parse and use the response data as needed
                data = response.json()
                print("API Response:", data)
                return True
            else:
                print(f"Error: {response.status_code} - {response.text}")
                response.raise_for_status()

            return response.id
        except FileNotFoundError as e:
            print(f"Error: {e}")
            raise e
        except ValueError as e:
            print(f"Error: {e}")
            raise e
        except Exception as e:
            # Handle any other unexpected exceptions here
            print(f"Unexpected Error: {e}")
            raise e

    def start(self):
        self.status(StatusEntity(Status.RUNNING))
    
    def end(self):
        self.status(StatusEntity(Status.FINISHED))

    def error(self, be:BaseException):        
        self.status(StatusEntity(Status.ERROR))
        self.sendExecutionLog(str(be)) 

class QCentroidSolverClient:
    # Init class with base parameters
    def __init__(self, base_url=None, api_key=None, solver_id=None):
        self.base_url = api_base_url #default production url
        
        if base_url is not None:
            self.base_url = base_url
        else:
            self.base_url = os.environ.get('QCENTROID_PUBLIC_API', api_base_url)
        if api_key is not None:             
            self.api_key = api_key
        else:
            self.api_key = os.environ.get('QCENTROID_AGENT_API_TOKEN')
        if solver_id is not None:             
            self.solver_id = solver_id
        else:
            self.solver_id = os.environ.get('QCENTROID_SOLVER_ID')

    def getHeaders(self):
        return {
            "X-API-Key": self.api_key,
            "Accept": "application/json",  # Set the content type based on your API's requirements
            "Content-Type": "application/json",  # Set the content type based on your API's requirements
        }
    #GET [core]/agent/job/{job_name}/data/input
    def obtainJob(self) -> QCentroidAgentClient:
        try:
            response = requests.get(f"{self.base_url}/agent/solver/{self.solver_id}/webhook", headers=self.getHeaders())

            
            match response.status_code:
                # Check if the request was successful (status code 200)            
                case 200:
                    # Parse and use the response data as needed
                    data = response.json()
                    print("API Response:", data)
                    return QCentroidAgentClient(self.base_url, data["token"], data["name"]) #return  QCentroidAgentClient
                
                # No jobs
                case 204:                
                    return None
                case _:
                    print(f"Error: {response.status_code} - {response.text}")
                    response.raise_for_status()

        except requests.RequestException as e:
            print(f"Request failed: {e}")
            raise e            
        except Exception as e:
            # Handle any exceptions or errors here
            print(f"Unexpected Error: {e}")
            raise e
