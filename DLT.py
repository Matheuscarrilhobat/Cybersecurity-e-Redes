import whois

sites = ["spotify.com", "google.com", "facebook.com", "twitter.com", "instagram.com"]

companies = [whois.whois(s).org for s in sites]
creation_dates = [whois.whois(s).creation_date for s in sites]

print(companies)
print(creation_dates)

emails = [whois.whois(s).emails for s in sites]

print(emails)
