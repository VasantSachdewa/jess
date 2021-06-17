import datetime
from typing import TypedDict, Dict, Union, List

from jess.libs.logs import Logs
from worker.extractors.extractor_interface import (ExtractedDataType,
                                                   JobExtractorInterface)
from bs4 import BeautifulSoup


logger = Logs.get_logger('Worker')


class JobsdbDetailExtractor(JobExtractorInterface):
    
    ID = 1
    
    def __init__(self, data: list):
        ''' data is list of unprocessed jobs'''
        self.raw_data = data
        
    def get_cleaned_data(self) -> List[ExtractedDataType]:
        logger.debug("Extracting data for seller {}".format(self.ID))
        job_detail = self.raw_data['data']['jobDetail']
        extracted_data = {
            'job_id': self._extract_job_id(job_detail),
            'page_url': self._extract_page_url(job_detail),
            'salary_max': self._extract_max_salary(job_detail),
            'salary_min': self._extract_max_salary(job_detail),
            'currency': 'THB',
            'job_title': self._extract_title(job_detail),
            'company': self._extract_company_name(job_detail),
            'post_date': self._extract_post_date(job_detail),
            'job_description': self._extract_job_description(job_detail),
            'job_requirements': self._extract_job_requirements(job_detail),
            'benefits': self._extract_benefits(job_detail),
            'industry': self._extract_industry(job_detail)
        }
            
        return extracted_data
        
    def _extract_job_id(self, job_detail: Dict) -> str:
        return job_detail['id']
    
    def _extract_page_url(self, job_detail: Dict) -> str:
        return job_detail['pageUrl']
    
    def _extract_min_salary(self, job_detail: Dict) -> Union[float, None]:
        try:
            return float(job_detail['header']['salary']['min'])
        except TypeError as e:
            logger.info("Failed extracting salary_min")
            return None
    
    def _extract_max_salary(self, job_detail: Dict) -> Union[float, None]:
        try:
            return float(job_detail['header']['salary']['max'])
        except TypeError as e:
            logger.info("Failed extracting salary_max")
    
    def _extract_title(self, job_detail: Dict) -> str:
        return job_detail['header']['jobTitle']
    
    def _extract_company_name(self, job_deatil: Dict) -> str:
        return job_deatil['header']['company']['name']
    
    def _extract_post_date(self, job_detail: Dict) -> str:
        try:
            datetime_obj = datetime.datetime.strptime(
                job_detail['header']['postedAt'], '%Y-%m-%dT%H:%M:%SZ')
        except ValueError:
            datetime_obj = datetime.datetime.strptime(
                job_detail['header']['postedAt'], '%Y-%m-%dT%H:%M:%S.%fZ')
            

        datetime_format = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')
        
        return datetime_format
    
    def _extract_job_description(self, job_detail: Dict) -> List[str]:
        return job_detail['jobDetail']['summary']
    
    def _extract_job_requirements(self, job_detail: Dict) -> List[str]:
        html = job_detail['jobDetail']['jobDescription']['html']
        soup = BeautifulSoup(html, 'html.parser')
        list_of_li = soup.find_all('li')
        job_requirements = list(map(lambda li: li.text, list_of_li))
        
        return job_requirements
    
    def _extract_benefits(self, job_detail: Dict) -> List[str]:
        return job_detail['jobDetail']['jobRequirement']['benefits']
            
    def _extract_industry(self, job_detail: Dict) -> str:
        return job_detail['jobDetail']['jobRequirement']['industryValue']['label']

