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
JOB_LISTING_API_RAW_RETURN = {
    "data": {
        "jobs": {
            "total": 3085,
            "totalJobs": 3085,
            "aigdpRelatedSearch": None,
            "relatedSearchKeywords": [],
            "solMetadata": {
                "requestToken": "35c79c49-08e9-4be7-ad41-4ffec5877195",
                "token": "0~35c79c49-08e9-4be7-ad41-4ffec5877195",
                "sortMode": "RELEVANCE",
                "categories": ["131"],
                "pageSize": 30,
                "pageNumber": 1,
                "totalJobCount": 3085,
                "tags": {
                    "mordor__flights": "mordor_58",
                    "jobsdb:userGroup": "B",
                },
            },
            "suggestedEmployer": None,
            "queryParameters": {"key": "", "searchFields": "", "pageSize": 30},
            "gdpSearchAlgoGroup": None,
            "experiments": {"flight": "mordor_58"},
            "jobs": [
                {
                    "id": "300003002373092",
                    "sourceCountryCode": "th",
                    "isStandout": True,
                    "companyMeta": {
                        "id": "210344",
                        "advertiserId": "th100130701",
                        "isPrivate": False,
                        "name": "Ajinomoto (Thailand) Co., Ltd.",
                        "logoUrl": "https://image-service-cdn.seek.com.au/732c73dacbdf56f687eae88aecdf07c069fd0040/ee4dce1061f3f616224767ad58cb2fc751b8d2dc",
                        "slug": "ajinomoto-thailand-co-ltd",
                    },
                    "jobTitle": "IT Infrastructure Staff  (Head Office, Phayathai)",
                    "jobUrl": "https://th.jobsdb.com/th/en/job/job-300003002373092?token=0~35c79c49-08e9-4be7-ad41-4ffec5877195&sectionRank=1&jobId=jobsdb-th-job-300003002373092",
                    "jobTitleSlug": "it-infrastructure-staff-head-office-phayathai",
                    "description": "Job Description: Maintain and monitor network, server, storage and facilities align with IT infrastructure security standard, IT service management...",
                    "employmentTypes": [
                        {"code": "full_time", "name": "Full Time"},
                        {"code": "permanent", "name": "Permanent"},
                    ],
                    "sellingPoints": [
                        "Bachelor Degree in Business Information System",
                        "At least 0-1 years of experience in infrastructure",
                        "Maintain and monitor network, server",
                    ],
                    "locations": [
                        {
                            "code": "39",
                            "name": "Phayathai",
                            "slug": "phayathai",
                            "children": None,
                        }
                    ],
                    "categories": [
                        {
                            "code": "131",
                            "name": "Information Technology (IT)",
                            "children": None,
                        },
                        {"code": "144", "name": "Security", "children": None},
                        {
                            "code": "147",
                            "name": "Network & System",
                            "children": None,
                        },
                        {"code": "150", "name": "Others", "children": None},
                    ],
                    "postingDuration": "19 hours ago",
                    "postedAt": "2021-06-02T17:03:59Z",
                    "salaryRange": {
                        "currency": None,
                        "max": None,
                        "min": None,
                        "period": "monthly",
                        "term": None,
                    },
                    "salaryVisible": False,
                    "bannerUrl": "https://image-service-cdn.seek.com.au/3d8b3f4c77520373e178cff2fcfe39a978f086d9/a868bcb8fbb284f4e8301904535744d488ea93c1",
                    "isClassified": False,
                    "solMetadata": {
                        "searchRequestToken": "35c79c49-08e9-4be7-ad41-4ffec5877195",
                        "token": "0~35c79c49-08e9-4be7-ad41-4ffec5877195",
                        "jobId": "jobsdb-th-job-300003002373092",
                        "section": "MAIN",
                        "sectionRank": 1,
                        "jobAdType": "ORGANIC",
                        "tags": {
                            "mordor__flights": "mordor_58",
                            "jobsdb:userGroup": "B",
                        },
                    },
                },
                {
                    "id": "300003002373745",
                    "sourceCountryCode": "th",
                    "isStandout": True,
                    "companyMeta": {
                        "id": "447603",
                        "advertiserId": "th300393149",
                        "isPrivate": False,
                        "name": "PRTR Recruitment and Outsourcing",
                        "logoUrl": "https://image-service-cdn.seek.com.au/72cf7c5dbc9931e6b59f85500796eb546d955ebe/ee4dce1061f3f616224767ad58cb2fc751b8d2dc",
                        "slug": "prtr-recruitment-and-outsourcing",
                    },
                    "jobTitle": "IT Assistant",
                    "jobUrl": "https://th.jobsdb.com/th/en/job/job-300003002373745?token=0~35c79c49-08e9-4be7-ad41-4ffec5877195&sectionRank=2&jobId=jobsdb-th-job-300003002373745",
                    "jobTitleSlug": "it-assistant",
                    "description": "Our client is an IT Solution provider including mobility as a service for transportation/Smart Office/Smart Factory/IoT/Telematics.Salary Max 35,000...",
                    "employmentTypes": [
                        {"code": "permanent", "name": "Permanent"}
                    ],
                    "sellingPoints": [
                        "Good Command of English",
                        "Basic Knowledge in IT Solution",
                        "Project Management Skills",
                    ],
                    "locations": [
                        {
                            "code": "34",
                            "name": "Pathumwan",
                            "slug": "pathumwan",
                            "children": None,
                        }
                    ],
                    "categories": [
                        {
                            "code": "131",
                            "name": "Information Technology (IT)",
                            "children": None,
                        },
                        {
                            "code": "132",
                            "name": "Application Specialist - Software",
                            "children": None,
                        },
                        {
                            "code": "147",
                            "name": "Network & System",
                            "children": None,
                        },
                        {"code": "150", "name": "Others", "children": None},
                    ],
                    "postingDuration": "19 hours ago",
                    "postedAt": "2021-06-02T17:05:49Z",
                    "salaryRange": {
                        "currency": None,
                        "max": None,
                        "min": None,
                        "period": "monthly",
                        "term": None,
                    },
                    "salaryVisible": False,
                    "bannerUrl": "https://image-service-cdn.seek.com.au/d382e6b0ed4d49f23f2ec84adb158a7d533bb277/a868bcb8fbb284f4e8301904535744d488ea93c1",
                    "isClassified": False,
                    "solMetadata": {
                        "searchRequestToken": "35c79c49-08e9-4be7-ad41-4ffec5877195",
                        "token": "0~35c79c49-08e9-4be7-ad41-4ffec5877195",
                        "jobId": "jobsdb-th-job-300003002373745",
                        "section": "MAIN",
                        "sectionRank": 2,
                        "jobAdType": "ORGANIC",
                        "tags": {
                            "mordor__flights": "mordor_58",
                            "jobsdb:userGroup": "B",
                        },
                    },
                },
                {
                    "id": "300003002369911",
                    "sourceCountryCode": "th",
                    "isStandout": True,
                    "companyMeta": {
                        "id": "509026",
                        "advertiserId": "th100130904",
                        "isPrivate": False,
                        "name": "Bangkokbank (BBL)",
                        "logoUrl": "https://image-service-cdn.seek.com.au/e8a09cfcf6326caf894ad78d196f5045f058eed9/ee4dce1061f3f616224767ad58cb2fc751b8d2dc",
                        "slug": "bangkokbank-bbl",
                    },
                    "jobTitle": "IT Security Administration",
                    "jobUrl": "https://th.jobsdb.com/th/en/job/job-300003002369911?token=0~35c79c49-08e9-4be7-ad41-4ffec5877195&sectionRank=3&jobId=jobsdb-th-job-300003002369911",
                    "jobTitleSlug": "it-security-administration",
                    "description": "??????????????????????????? ????????????????????????????????????????????????????????????????????????????????????????????? \xa0Security Software \xa0?????????\xa0Tool\xa0???????????? ??? ????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????...",
                    "employmentTypes": [
                        {"code": "full_time", "name": "Full Time"},
                        {"code": "permanent", "name": "Permanent"},
                    ],
                    "sellingPoints": [
                        "IT Security Admin",
                        "Mainframe, AS/400, Unix, Oracle, SQL, Tandem, Wind",
                        "Information security",
                    ],
                    "locations": [
                        {
                            "code": "13",
                            "name": "Bangrak",
                            "slug": "bangrak",
                            "children": None,
                        }
                    ],
                    "categories": [
                        {
                            "code": "131",
                            "name": "Information Technology (IT)",
                            "children": None,
                        },
                        {"code": "139", "name": "Support", "children": None},
                        {"code": "144", "name": "Security", "children": None},
                        {"code": "150", "name": "Others", "children": None},
                    ],
                    "postingDuration": "19 hours ago",
                    "postedAt": "2021-06-02T17:02:43Z",
                    "salaryRange": {
                        "currency": None,
                        "max": None,
                        "min": None,
                        "period": "monthly",
                        "term": None,
                    },
                    "salaryVisible": False,
                    "bannerUrl": "https://image-service-cdn.seek.com.au/55446f395c6a1c86a3ec71bc07752aee6955f769/a868bcb8fbb284f4e8301904535744d488ea93c1",
                    "isClassified": False,
                    "solMetadata": {
                        "searchRequestToken": "35c79c49-08e9-4be7-ad41-4ffec5877195",
                        "token": "0~35c79c49-08e9-4be7-ad41-4ffec5877195",
                        "jobId": "jobsdb-th-job-300003002369911",
                        "section": "MAIN",
                        "sectionRank": 3,
                        "jobAdType": "ORGANIC",
                        "tags": {
                            "mordor__flights": "mordor_58",
                            "jobsdb:userGroup": "B",
                        },
                    },
                },
            ],
        }
    }
}
JOB_LISTINGS = [
    {
        "id": "",
        "sourceCountryCode": "th",
        "isStandout": False,
        "companyMeta": {
            "id": "447786",
            "advertiserId": "th300350740",
            "isPrivate": False,
            "name": "Rugby School Thailand",
            "logoUrl": "",
            "slug": "rugby-school-thailand",
        },
        "jobTitle": "Data Protection Officer",
        "jobUrl": "https://th.jobsdb.com/th/en/job/job-300003002365458?token=0~ca9e9e4d-407e-4702-855f-bdda5f74ea5c&sectionRank=1&jobId=jobsdb-th-job-300003002365458",
        "jobTitleSlug": "data-protection-officer",
        "description": "The health, safety and well-being of young people are of paramount importance to all the adults who work at Rugby School Thailand. Children have the...",
        "employmentTypes": [
            {"code": "full_time", "name": "Full Time"},
            {"code": "permanent", "name": "Permanent"},
        ],
        "sellingPoints": [],
        "locations": [
            {
                "code": "89",
                "name": "Eastern",
                "slug": "eastern",
                "children": None,
            }
        ],
        "categories": [
            {
                "code": "131",
                "name": "Information Technology (IT)",
                "children": None,
            },
            {"code": "134", "name": "DBA", "children": None},
            {"code": "144", "name": "Security", "children": None},
            {"code": "285", "name": "Professional Services", "children": None},
            {"code": "160", "name": "Legal & Compliance", "children": None},
        ],
        "postingDuration": "10 hours ago",
        "postedAt": "2021-06-01T23:00:01Z",
        "salaryRange": {
            "currency": None,
            "max": None,
            "min": None,
            "period": "monthly",
            "term": None,
        },
        "salaryVisible": False,
        "bannerUrl": "",
        "isClassified": False,
        "solMetadata": {
            "searchRequestToken": "ca9e9e4d-407e-4702-855f-bdda5f74ea5c",
            "token": "0~ca9e9e4d-407e-4702-855f-bdda5f74ea5c",
            "jobId": "jobsdb-th-job-300003002365458",
            "section": "MAIN",
            "sectionRank": 1,
            "jobAdType": "ORGANIC",
            "tags": {"mordor__flights": "mordor_58", "jobsdb:userGroup": "B"},
        },
    },
    {
        "id": "",
        "sourceCountryCode": "th",
        "isStandout": True,
        "companyMeta": {
            "id": "jobsdb-th-300396993",
            "advertiserId": "th300396993",
            "isPrivate": False,
            "name": "EDM Corporation Co., Ltd.",
            "logoUrl": "https://image-service-cdn.seek.com.au/583acef6a1c758b89331865969329a33c2edb3ad/ee4dce1061f3f616224767ad58cb2fc751b8d2dc",
            "slug": "edm-corporation-co-ltd",
        },
        "jobTitle": "Customer Service/??????????????????????????????????????????????????????",
        "jobUrl": "https://th.jobsdb.com/th/en/job/job-300003002364354?token=0~ca9e9e4d-407e-4702-855f-bdda5f74ea5c&sectionRank=2&jobId=jobsdb-th-job-300003002364354",
        "jobTitleSlug": "customer-service-??????????????????????????????????????????????????????",
        "description": "????????????????????????????????????????????????????????????????????? ???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????? ????????????????????????????????????????????????????????????????????? ???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????...",
        "employmentTypes": [
            {"code": "full_time", "name": "Full Time"},
            {"code": "permanent", "name": "Permanent"},
        ],
        "sellingPoints": [
            "Company in stability",
            "Free Lunch / Beverages",
            "Monthly Bonus",
        ],
        "locations": [
            {
                "code": "8",
                "name": "Bangkoknoi",
                "slug": "bangkoknoi",
                "children": None,
            }
        ],
        "categories": [
            {
                "code": "233",
                "name": "Sales, CS & Business Devpt",
                "children": None,
            },
            {"code": "67", "name": "Customer Service", "children": None},
            {
                "code": "131",
                "name": "Information Technology (IT)",
                "children": None,
            },
            {"code": "139", "name": "Support", "children": None},
            {"code": "243", "name": "Others", "children": None},
        ],
        "postingDuration": "31-May-21",
        "postedAt": "2021-05-31T23:00:00Z",
        "salaryRange": {
            "currency": None,
            "max": None,
            "min": None,
            "period": "monthly",
            "term": None,
        },
        "salaryVisible": False,
        "bannerUrl": "https://image-service-cdn.seek.com.au/80dc20e65f6dd9547a0dbe586ce91783ef262e2e/a868bcb8fbb284f4e8301904535744d488ea93c1",
        "isClassified": False,
        "solMetadata": {
            "searchRequestToken": "ca9e9e4d-407e-4702-855f-bdda5f74ea5c",
            "token": "0~ca9e9e4d-407e-4702-855f-bdda5f74ea5c",
            "jobId": "jobsdb-th-job-300003002364354",
            "section": "MAIN",
            "sectionRank": 2,
            "jobAdType": "ORGANIC",
            "tags": {"mordor__flights": "mordor_58", "jobsdb:userGroup": "B"},
        },
    },
    {
        "id": "",
        "sourceCountryCode": "th",
        "isStandout": True,
        "companyMeta": {
            "id": "jobsdb-th-300301094",
            "advertiserId": "th300301094",
            "isPrivate": False,
            "name": "SATO KOKI (THAILAND) CO., LTD.",
            "logoUrl": "",
            "slug": "sato-koki-thailand-co-ltd",
        },
        "jobTitle": "IT Staff/????????????????????????????????? IT",
        "jobUrl": "https://th.jobsdb.com/th/en/job/job-300003002376339?token=0~ca9e9e4d-407e-4702-855f-bdda5f74ea5c&sectionRank=3&jobId=jobsdb-th-job-300003002376339",
        "jobTitleSlug": "it-staff-?????????????????????????????????-it",
        "description": "???????????????????????????\xa0\xa0 \xa0 \xa0????????????????????????????????? ERP\xa0 ?????????????????????????????????????????????????????????????????????????????????\xa0??????????????????????????? ?????????????????????????????????\xa0\xa0 ?????????????????????????????? ?????????????????????????????????????????? ?????????????????????????????????????????????,IT ???????????????????????????????????????????????????...",
        "employmentTypes": [{"code": "full_time", "name": "Full Time"}],
        "sellingPoints": [
            "???????????????????????????????????? Program PostgreSQL ?????????",
            "???????????????????????????????????? Program Open ERP (V7) ?????????????????????????????????Odoo",
            "??????????????????????????????????????????????????????????????????????????? Ubuntu Server ?????????",
        ],
        "locations": [
            {
                "code": "63",
                "name": "Ladlumkaew",
                "slug": "ladlumkaew",
                "children": None,
            }
        ],
        "categories": [
            {
                "code": "131",
                "name": "Information Technology (IT)",
                "children": None,
            },
            {"code": "139", "name": "Support", "children": None},
        ],
        "postingDuration": "7 hours ago",
        "postedAt": "2021-06-02T01:37:06Z",
        "salaryRange": {
            "currency": None,
            "max": None,
            "min": None,
            "period": "monthly",
            "term": None,
        },
        "salaryVisible": False,
        "bannerUrl": "https://image-service-cdn.seek.com.au/cc25c974d7d175aeb84549e6d0a7ed171a11446e/a868bcb8fbb284f4e8301904535744d488ea93c1",
        "isClassified": False,
        "solMetadata": {
            "searchRequestToken": "ca9e9e4d-407e-4702-855f-bdda5f74ea5c",
            "token": "0~ca9e9e4d-407e-4702-855f-bdda5f74ea5c",
            "jobId": "jobsdb-th-job-300003002376339",
            "section": "MAIN",
            "sectionRank": 3,
            "jobAdType": "ORGANIC",
            "tags": {"mordor__flights": "mordor_58", "jobsdb:userGroup": "B"},
        },
    },
]
