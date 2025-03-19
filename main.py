# LinkedIn URL Generator for Recent Job Posts

import urllib.parse

def generate_linkedin_job_url(keywords, geo_id, hours, distance=25):
    base_url = "https://www.linkedin.com/jobs/search/"

    # Convert hours into seconds
    seconds = hours * 3600

    params = {
        "keywords": keywords,
        "geoId": geo_id,
        "f_TPR": f"r{seconds}",
        "distance": distance,
        "sortBy": "DD",  # Sort by date posted descending
    }

    # Encode parameters properly
    param_str = urllib.parse.urlencode(params)
    final_url = f"{base_url}?{param_str}"

    return final_url


def main():
    keywords = input("Enter the job keywords or role: ")
    geo_id = input("Enter LinkedIn geo ID (e.g., 102454443 for Singapore): ")
    hours = float(input("Enter how recent (in hours) the job posts should be: "))
    distance = input("Enter search distance in km/miles (default is 25, press enter to keep default): ")

    distance = int(distance) if distance else 25

    url = generate_linkedin_job_url(keywords, geo_id, hours, distance)

    print("\nYour LinkedIn job search URL:")
    print(url)


if __name__ == '__main__':
    main()
