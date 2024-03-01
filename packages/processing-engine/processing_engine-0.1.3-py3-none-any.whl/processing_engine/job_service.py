from typing import List
import psycopg2
import psycopg2.extras
from processing_engine.dda_models import LogMessage
from processing_engine.class_helpers import Utils

class JobService():
    """
    Tracks errors and log Messages, single instance of connection requirements, passed around. Gets reset and instantiated by the Enhancement Manager each time a new event is processed.
    To keep track of:
    - DBengine: DBengine to be used to query the database.
    - processing_guid

    - last_error_message
    - last_error_time

    - item count
    - s3_key
    - integration_name
    - integration_version

    - adapter used.
    - organization_guid


    - array of log_messages

    Methods:
    - Filter count of error messages
    - Add Error Message



    Messages Log Tracking requires of.
    - log_date
    - event_guid
    - log_type
    - log_message
    - log_detail
    """

    def __init__(self,  username: str, password: str, host: str, database: str,
                 organization_guid: str, 
                 connector_guid: str,
                 processing_guid: str,
                 
                 integration_name: str,


                  job_parameters: dict):
        
        # Key Parameters: postgresql credentials
        self.connection = psycopg2.connect(
            user=username,
            password=password,
            host=host,
            database=database
        )

        self.cursor = self.connection.cursor(
            cursor_factory=psycopg2.extras.DictCursor
        )

        self.cursor.execute(
            "SELECT id FROM organization WHERE guid = '123e4567-e89b-12d3-a456-1231231'")
        organization_id = self.cursor.fetchone()
        if organization_id is None:
            raise ValueError("Organization not found")
        print(organization_id)

        self.connector_guid = connector_guid

        # For processiing type, you do need to 

        self.organization_guid = organization_guid
        self.processing_guid = processing_guid
        self.integration_name = integration_name

        self.integration_version = Utils.NoneSafe(job_parameters, 'integration_version')


        self.s3_key = Utils.NoneSafe(job_parameters, 's3_key')
        self.item_count = Utils.NoneSafe(job_parameters, 'item_count')
        self.adapter = Utils.NoneSafe(job_parameters, 'adapter') # Adapter used to process the data.
        self.event_date = Utils.NoneSafe(job_parameters, 'event_date')

        self.log_messages: List[LogMessage] = []
        self.last_error_message = None
        self.last_error_time = None

    def addLogMessage(self, log_message: str, log_detail: str, log_type: str = 'Error', log_console: bool = True):
        self.log_messages.append(LogMessage(log_type, log_message, log_detail))
        self.last_error_message = log_message
        self.last_error_time = Utils.getNow()
        if log_console:
            print(log_message, log_detail)
        
    def startProcessingStatus(self):
        self.cursor.execute(
            f"INSERT INTO processing_tracker (processing_guid, status, source_guid, s3_key, organization_guid, integration_name, source_date, task, start_time, received_time) VALUES ('{self.processing_guid}', 'PROCESSING', '{self.processing_guid}', '{self.s3_key}', '{self.organization_guid}', '{self.integration_name}', '{self.event_date}', 'TIMESLOT PROCESSING', '{Utils.getNow()}', '{Utils.getNow()}'"
        )
        self.connection.commit()
        
    def changeProcessingStatus(self, status: str):
        self.cursor.execute(
            f"UPDATE processing_tracker SET status = '{status}' WHERE processing_guid = '{self.processing_guid}'"
        )
        self.connection.commit()

    def endProcessingStatus(self):
        self.cursor.execute(
            f"UPDATE processing_tracker SET status = 'COMPLETE', end_time = '{Utils.getNow()}' WHERE processing_guid = '{self.processing_guid}'"
        )
        self.connection.commit()

    # destroy overwrite. ensure that the connection is closed.
    def __del__(self):
        self.connection.close()
        self.cursor.close()
        self.connection = None
        self.cursor = None
