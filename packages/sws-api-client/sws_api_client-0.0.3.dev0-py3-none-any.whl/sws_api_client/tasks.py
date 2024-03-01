from sws_api_client.sws_api_client import SwsApiClient
from dataclasses import dataclass
from typing import List, Dict, Optional, Literal

@dataclass
class TaskDataset:
    domain: str
    dataset: str

@dataclass
class TaskParameters:
    param1: str
    param2: str

@dataclass
class TaskPayload:
    datasets: List[TaskDataset]
    parameters: TaskParameters

# Define Status and DetailStatus as Literal types
Status = Literal['ACTIVE', 'ARCHIVED']
DetailStatus = Literal['CREATED', 'EXECUTION_PREPARED', 'EXECUTION_PROCESSING', 'EXECUTION_PROCESSED', 'STOP_REQUESTED', 'RETRIED', 'ENDED', 'ARCHIVED']

@dataclass
class TaskInfo:
    detail_status: DetailStatus
    ended_on: str
    description: str
    updated_on: str
    created_on: str
    service_user: str
    tags: Dict[str, str]
    output: Dict[str, str]
    input: str
    task_type: str
    context: str
    progress: int
    user: str
    outcome: str
    status: Status

@dataclass
class TaskResponse:
    task_id: str
    info: TaskInfo

class TaskManager:

    def __init__(self, sws_client: SwsApiClient, endpoint: str = 'task_manager_api') -> None:
        self.sws_client = sws_client
        self.endpoint = endpoint

    def updateCurrent(self, progress: Optional[int] = None) -> dict:
        if not self.sws_client.current_task_id:
            raise ValueError("A current task ID must be provided.")
        if not self.sws_client.current_execution_id:
            raise ValueError("A current task ID must be provided.")
        taskId = self.sws_client.current_task_id
        executionId = self.sws_client.current_execution_id

        path = f'/task/{taskId}/execution/{executionId}/status'
        data = {
            'progress': progress
        }
        self.sws_client.discoverable.put(self.endpoint, path, data=data)

    def create(self, task_payload: TaskPayload, task_group: Optional[str] = None) -> dict:
        path = '/create'

        data = {
            'task_payload': task_payload
        }

        if task_group:
            data['task_group'] = task_group

        return self.sws_client.discoverable.post(self.endpoint, path, data=data)

    def get_task(self, task_id: str) -> Optional[TaskResponse]:
        path = f'/task/{task_id}'
        response = self.sws_client.discoverable.get(self.endpoint, path)

        if response:
            return TaskResponse(
                task_id=response.get('taskId'),
                info=TaskInfo(
                    detail_status=response['info']['detailStatus'],
                    ended_on=response['info']['endedOn'],
                    description=response['info']['description'],
                    updated_on=response['info']['updatedOn'],
                    created_on=response['info']['createdOn'],
                    service_user=response['info']['serviceUser'],
                    tags=response['info']['tags'],
                    output=response['info']['output'],
                    input=response['info']['input'],
                    task_type=response['info']['taskType'],
                    context=response['info']['context'],
                    progress=response['info']['progress'],
                    user=response['info']['user'],
                    outcome=response['info']['outcome'],
                    status=response['info']['status']
                )
            )
        else:
            return None