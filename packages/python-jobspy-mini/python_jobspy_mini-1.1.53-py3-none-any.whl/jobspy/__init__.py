import datetime
from typing import Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed

from .jobs import JobType, Location, JobPost, Compensation, DescriptionFormat
from .scrapers.indeed import IndeedScraper
from .scrapers.ziprecruiter import ZipRecruiterScraper
from .scrapers.glassdoor import GlassdoorScraper
from .scrapers.linkedin import LinkedInScraper
from .scrapers import ScraperInput, Site, JobResponse, Country
from .scrapers.exceptions import (
    LinkedInException,
    IndeedException,
    ZipRecruiterException,
    GlassdoorException,
)


def scrape_jobs(
        site_name: str | list[str] | Site | list[Site] | None = None,
        search_term: str | None = None,
        location: str | None = None,
        distance: int | None = None,
        is_remote: bool = False,
        job_type: str | None = None,
        easy_apply: bool | None = None,
        results_wanted: int = 15,
        country_indeed: str = "usa",
        hyperlinks: bool = False,
        proxy: str | None = None,
        description_format: DescriptionFormat = "markdown",
        linkedin_fetch_description: bool | None = False,
        linkedin_company_ids: list[int] | None = None,
        offset: int | None = 0,
        hours_old: int = None,
        **kwargs,
) -> list[JobPost]:
    """
    Simultaneously scrapes job data from multiple job sites.
    :return: results_wanted: pandas dataframe containing job data
    """
    SCRAPER_MAPPING = {
        Site.LINKEDIN: LinkedInScraper,
        Site.INDEED: IndeedScraper,
        Site.ZIP_RECRUITER: ZipRecruiterScraper,
        Site.GLASSDOOR: GlassdoorScraper,
    }

    def map_str_to_site(site_name: str) -> Site:
        return Site[site_name.upper()]

    def get_enum_from_value(value_str):
        for job_type in JobType:
            if value_str in job_type.value:
                return job_type
        raise Exception(f"Invalid job type: {value_str}")

    job_type = get_enum_from_value(job_type) if job_type else None

    def get_site_type():
        site_types = list(Site)
        if isinstance(site_name, str):
            site_types = [map_str_to_site(site_name)]
        elif isinstance(site_name, Site):
            site_types = [site_name]
        elif isinstance(site_name, list):
            site_types = [
                map_str_to_site(site) if isinstance(site, str) else site
                for site in site_name
            ]
        return site_types

    country_enum = Country.from_string(country_indeed)

    scraper_input = ScraperInput(
        site_type=get_site_type(),
        country=country_enum,
        search_term=search_term,
        location=location,
        distance=distance,
        is_remote=is_remote,
        job_type=job_type,
        easy_apply=easy_apply,
        description_format=description_format,
        linkedin_fetch_description=linkedin_fetch_description,
        results_wanted=results_wanted,
        linkedin_company_ids=linkedin_company_ids,
        offset=offset,
        hours_old=hours_old
    )

    def scrape_site(site: Site) -> Tuple[str, JobResponse]:
        scraper_class = SCRAPER_MAPPING[site]
        scraper = scraper_class(proxy=proxy)
        scraped_data: JobResponse = scraper.scrape(scraper_input)
        return site.value, scraped_data

    site_to_jobs_dict: dict[str, JobResponse] = {}

    def worker(site):
        site_val, scraped_info = scrape_site(site)
        return site_val, scraped_info

    with ThreadPoolExecutor() as executor:
        future_to_site = {
            executor.submit(worker, site): site for site in scraper_input.site_type
        }

        for future in as_completed(future_to_site):
            site_value, scraped_data = future.result()
            site_to_jobs_dict[site_value] = scraped_data

    jobs_dfs: list[JobPost] = []

    for site, job_response in site_to_jobs_dict.items():
        for job in job_response.jobs:
            jobs_dfs.append(job)

            # job_data[
            #     "job_url_hyper"
            # ] = f'<a href="{job_data["job_url"]}">{job_data["job_url"]}</a>'
            # job_data["site"] = site
            # job_data["company"] = job_data["company_name"]

            # job.job_type = (
            #     ", ".join(job_type.value[0] for job_type in job.job_type)
            #     if job.job_type
            #     else None
            # )
            # job.emails = (
            #     ", ".join(job.emails) if job.emails else None
            # )
            # if job.location:
            #     job.location = Location(
            #         **job.location
            #     ).display_location()
            #
            # compensation_obj = job_data.get("compensation")
            # if compensation_obj and isinstance(compensation_obj, dict):
            #     job_data["interval"] = (
            #         compensation_obj.get("interval").value
            #         if compensation_obj.get("interval")
            #         else None
            #     )
            #     job_data["min_amount"] = compensation_obj.get("min_amount")
            #     job_data["max_amount"] = compensation_obj.get("max_amount")
            #     job_data["currency"] = compensation_obj.get("currency", "USD")
            # else:
            #     job_data["interval"] = None
            #     job_data["min_amount"] = None
            #     job_data["max_amount"] = None
            #     job_data["currency"] = None
            #
            # jobs_dfs.append(JobPost(
            #     title=job_data["title"],
            #     company_name=job_data["company"],
            #     location=job_data["location"],
            #     date_posted=job_data["date_posted"],
            #     job_url=job_data["job_url"],
            #     company_url=job_data["company_url"],
            #     job_type=job_data["job_type"],
            #     description=job_data["description"],
            #     is_remote=job_data["is_remote"],
            #     num_urgent_words=job_data["num_urgent_words"],
            #     benefits=job_data["benefits"],
            #     emails=job_data["emails"],
            #     compensation=Compensation(
            #         interval=job_data["interval"],
            #         min_amount=job_data["min_amount"],
            #         max_amount=job_data["max_amount"],
            #         currency=job_data["currency"],
            #     ),
            # ))

    return jobs_dfs
