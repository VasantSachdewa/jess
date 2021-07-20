from typing import TypedDict, Union, List


class ExtractedDataType(TypedDict):
    job_id: str
    page_url: str
    salary_min: Union[float, None]
    salary_max: float
    currency: str
    job_title: str
    company: str
    post_date: str
    job_description: List[str]
    job_requirements: List[str]
    benefits: List[str]
    industry: str


class JobExtractorInterface:
    def __init__(self, data: list):
        raise NotImplementedError

    def get_cleaned_data(self) -> ExtractedDataType:
        raise NotImplementedError
