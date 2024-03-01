
from processing_engine.dda_models import *
from processing_engine.job_service import *
from processing_engine.processing_abstract import *
from processing_engine.processing_concrete import *
from processing_engine.adapters import *



import pytest
import json
import pprint

class TestAdapter:

    @pytest.fixture(scope='function')
    def job_service(self):
        job_service = JobService(
            username="postgres",
            password="dDueller123araM=!",
            host="test-ddanalytics-rds-v2.cpcwi20k2qgg.us-east-1.rds.amazonaws.com",
            database="v1_2",
            organization_guid="123e4567-e89b-12d3-a456-1231231",
            connector_guid="077b0fe8-98d8-4cc1-859b-4c9125d9d38b",
            processing_guid="65dc302d-d591-4634-a531-a5eae45e182b",
            integration_name="Salesforce",
            job_parameters={}
        )
        return job_service



    def test_adapts_salesforce(self, job_service):
        salesforce_integration_adapter = SalesforceIntegrationAdapter()
        sample_events = json.load(open('tests/data/events_sf.json'))
        
        adapted_events: List[EventData] = salesforce_integration_adapter.adapt(sample_events, job_service)
        print("=========== Adapted Event Sample from Salesforce ============")
        pprint.pprint(adapted_events[0].__dict__)

        assert adapted_events[0].user_id == 277
        assert adapted_events[0].local_timezone == "America/Los_Angeles"


    def test_adapts_windows(self, job_service):
        windows_integration_adapter = WindowsIntegrationAdapter()
        sample_events = json.load(open('tests/data/events_windows.json'))

        adapted_events: List[EventData] = windows_integration_adapter.adapt(sample_events, job_service)
        print("=========== Adapted Event Sample from Windows ============")
        pprint.pprint(adapted_events[0].__dict__)

    
