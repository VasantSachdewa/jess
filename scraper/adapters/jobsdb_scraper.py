import json
from typing import List

import requests
from jess.libs.logs import Logs
from jess.libs.metrics_tracker import STATSD_CLIENT
from scraper.adapters.job_scraper_interface import JobScraperInterface
from scraper.exceptions.request_exceptions import (
    JobsdbDetailRequestError,
    JobsdbListingRequestError,
)

logger = Logs.get_logger("Scraper")

JOB_LISTING_ENDPOINT = "https://xapi.supercharge-srp.co/job-search/graphql?country=th&isSmartSearch=true"
LISTING_REQUEST_BODY = {
    "query": "query getJobs($country: String, $locale: String, $keyword: String, $createdAt: String, $jobFunctions: [Int], $categories: [String], $locations: [Int], $careerLevels: [Int], $minSalary: Int, $maxSalary: Int, $salaryType: Int, $candidateSalary: Int, $candidateSalaryCurrency: String, $datePosted: Int, $jobTypes: [Int], $workTypes: [String], $industries: [Int], $page: Int, $pageSize: Int, $companyId: String, $advertiserId: String, $userAgent: String, $accNums: Int, $subAccount: Int, $minEdu: Int, $maxEdu: Int, $edus: [Int], $minExp: Int, $maxExp: Int, $seo: String, $searchFields: String, $candidateId: ID, $isDesktop: Boolean, $isCompanySearch: Boolean, $sort: String, $sVi: String, $duplicates: String, $flight: String, $solVisitorId: String) {\n  jobs(country: $country, locale: $locale, keyword: $keyword, createdAt: $createdAt, jobFunctions: $jobFunctions, categories: $categories, locations: $locations, careerLevels: $careerLevels, minSalary: $minSalary, maxSalary: $maxSalary, salaryType: $salaryType, candidateSalary: $candidateSalary, candidateSalaryCurrency: $candidateSalaryCurrency, datePosted: $datePosted, jobTypes: $jobTypes, workTypes: $workTypes, industries: $industries, page: $page, pageSize: $pageSize, companyId: $companyId, advertiserId: $advertiserId, userAgent: $userAgent, accNums: $accNums, subAccount: $subAccount, minEdu: $minEdu, edus: $edus, maxEdu: $maxEdu, minExp: $minExp, maxExp: $maxExp, seo: $seo, searchFields: $searchFields, candidateId: $candidateId, isDesktop: $isDesktop, isCompanySearch: $isCompanySearch, sort: $sort, sVi: $sVi, duplicates: $duplicates, flight: $flight, solVisitorId: $solVisitorId) {\n    ...LegacyCompat_SearchResult\n    relatedSearchKeywords {\n      keywords\n      type\n      totalJobs\n    }\n  }\n}\n\nfragment LegacyCompat_SearchResult on SearchResult {\n  total\n  totalJobs\n  aigdpRelatedSearch\n  relatedSearchKeywords {\n    keywords\n    type\n    totalJobs\n  }\n  solMetadata\n  suggestedEmployer {\n    name\n    totalJobs\n  }\n  queryParameters {\n    key\n    searchFields\n    pageSize\n  }\n  gdpSearchAlgoGroup\n  experiments {\n    flight\n  }\n  jobs {\n    id\n    sourceCountryCode\n    isStandout\n    companyMeta {\n      id\n      advertiserId\n      isPrivate\n      name\n      logoUrl\n      slug\n    }\n    jobTitle\n    jobUrl\n    jobTitleSlug\n    description\n    employmentTypes {\n      code\n      name\n    }\n    sellingPoints\n    locations {\n      code\n      name\n      slug\n      children {\n        code\n        name\n        slug\n      }\n    }\n    categories {\n      code\n      name\n      children {\n        code\n        name\n      }\n    }\n    postingDuration\n    postedAt\n    salaryRange {\n      currency\n      max\n      min\n      period\n      term\n    }\n    salaryVisible\n    bannerUrl\n    isClassified\n    solMetadata\n  }\n}\n",
    "variables": {
        "keyword": "",
        "jobFunctions": [131],
        "locations": [],
        "salaryType": 1,
        "jobTypes": [],
        "createdAt": None,
        "careerLevels": [],
        "page": 1,
        "country": "th",
        "sVi": "[CS]v1|30471EFC7EA3D18B-40000871C53FD95B[CE]",
        "solVisitorId": "6c0e00aa-d5f5-442b-88ed-afd225df3e92",
        "categories": ["131"],
        "workTypes": [],
        "userAgent": "Mozilla/5.0%20(Macintosh;%20Intel%20Mac%20OS%20X%2010_15_7)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/90.0.4430.212%20Safari/537.36",
        "industries": [],
        "locale": "en",
    },
}
JOB_DETAIL_REQUEST_BODY = {
    "query": "query getJobDetail($jobId: String, $locale: String, $country: String, $candidateId: ID, $solVisitorId: String, $flight: String) {\n  jobDetail(jobId: $jobId, locale: $locale, country: $country, candidateId: $candidateId, solVisitorId: $solVisitorId, flight: $flight) {\n    id\n    pageUrl\n    jobTitleSlug\n    applyUrl {\n      url\n      isExternal\n    }\n    isExpired\n    isConfidential\n    isClassified\n    accountNum\n    advertisementId\n    subAccount\n    showMoreJobs\n    adType\n    header {\n      banner {\n        bannerUrls {\n          large\n        }\n      }\n      salary {\n        max\n        min\n        type\n        extraInfo\n        currency\n        isVisible\n      }\n      logoUrls {\n        small\n        medium\n        large\n        normal\n      }\n      jobTitle\n      company {\n        name\n        url\n        slug\n        advertiserId\n      }\n      review {\n        rating\n        numberOfReviewer\n      }\n      expiration\n      postedDate\n      postedAt\n      isInternship\n    }\n    companyDetail {\n      companyWebsite\n      companySnapshot {\n        avgProcessTime\n        registrationNo\n        employmentAgencyPersonnelNumber\n        employmentAgencyNumber\n        telephoneNumber\n        workingHours\n        website\n        facebook\n        size\n        dressCode\n        nearbyLocations\n      }\n      companyOverview {\n        html\n      }\n      videoUrl\n      companyPhotos {\n        caption\n        url\n      }\n    }\n    jobDetail {\n      summary\n      jobDescription {\n        html\n      }\n      jobRequirement {\n        careerLevel\n        yearsOfExperience\n        qualification\n        fieldOfStudy\n        industryValue {\n          value\n          label\n        }\n        skills\n        employmentType\n        languages\n        postedDate\n        closingDate\n        jobFunctionValue {\n          code\n          name\n          children {\n            code\n            name\n          }\n        }\n        benefits\n      }\n      whyJoinUs\n    }\n    location {\n      location\n      locationId\n      omnitureLocationId\n    }\n    sourceCountry\n  }\n}\n",
    "variables": {
        "jobId": "",
        "country": "th",
        "locale": "en",
        "candidateId": "",
        "solVisitorId": "6c0e00aa-d5f5-442b-88ed-afd225df3e92",
    },
}
HEADER = {
    "authority": "xapi.supercharge-srp.co",
    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    "sec-ch-ua-mobile": "?0",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "content-type": "application/json",
    "accept": "*/*",
    "origin": "https://th.jobsdb.com",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://th.jobsdb.com/",
    "accept-language": "en-US,en;q=0.9",
}


class JobsdbScraper(JobScraperInterface):

    ENDPOINT = JOB_LISTING_ENDPOINT
    LISTING_REQUEST_BODY = LISTING_REQUEST_BODY
    JOB_DETAIL_REQUEST_BODY = JOB_DETAIL_REQUEST_BODY
    HEADER = HEADER
    _ID = 1

    @STATSD_CLIENT.timer('scraper.JobsdbScraper.get_posts')
    def get_posts(self, post_count: int = 10) -> List:
        job_listings = self.get_job_detail_list(post_count)

        return job_listings

    @STATSD_CLIENT.timer('scraper.JobsdbScraper.get_job_detail_list')
    def get_job_detail_list(self, post_count: int) -> List:
        """
        the method is responsible for returning list
        of job details
        """
        job_listings = self.get_job_listings(post_count)
        logger.debug("Making request to endpoint {}".format(self.ENDPOINT))
        job_details_list = []
        # TO-DO iterating twice, find a work around
        for job in job_listings:
            job_id = job["id"]
            logger.debug("Getting job info for id {}".format(job_id))
            self.JOB_DETAIL_REQUEST_BODY["variables"]["jobId"] = job_id
            try:
                resp = requests.post(
                    url=self.ENDPOINT,
                    data=json.dumps(self.JOB_DETAIL_REQUEST_BODY),
                    headers=self.HEADER,
                )
                if resp.status_code != 200:
                    raise JobsdbDetailRequestError(
                        self.ENDPOINT, resp.status_code, resp.content
                    )
                data = resp.json()
            except JobsdbDetailRequestError:
                logger.error("Failed to request job_id {}".format(job_id))
                continue
            except Exception as e:
                logger.error("Failed request with error {}".format(e))
                continue
            job_details_list.append(data)

        return job_details_list

    @STATSD_CLIENT.timer('scraper.JobsdbScraper.get_job_listings')
    def get_job_listings(self, post_count: int) -> List:
        """
        the method is responsbile for returning listing
        of jobs with minimal detail
        """
        job_listings = []
        logger.debug("Making request to endpoint {}".format(self.ENDPOINT))
        page_number = 1
        while len(job_listings) < post_count and page_number < 10:
            self.LISTING_REQUEST_BODY["variables"]["page"] = page_number
            try:
                resp = requests.post(
                    url=self.ENDPOINT,
                    data=json.dumps(self.LISTING_REQUEST_BODY),
                    headers=self.HEADER,
                )
                if resp.status_code != 200:
                    raise JobsdbListingRequestError(
                        self.ENDPOINT, resp.status_code, resp.content
                    )
                data = resp.json()
            except JobsdbListingRequestError:
                logger.error(
                    "Failed request for page_number {}".format(page_number)
                )
                return []
            except Exception as e:
                logger.error("Failed request with error {}".format(e))
                return []
            job_listings.extend(data["data"]["jobs"]["jobs"])
            page_number = page_number + 1

        return job_listings


if __name__ == "__main__":
    scraper = JobsdbScraper()
    scraper.get_job_listings(30)
