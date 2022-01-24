import unicodecsv as csv
from faker import Factory
from collections import defaultdict
def anonymize_rows(rows):
    """
    Rows is an iterable of dictionaries that contain name and
    email fields that need to be anonymized.
    """
    # Load the faker and its providers
    faker  = Factory.create()
    # Create mappings of names & emails to faked names & emails.
    names  = defaultdict(faker.name)
    emails = defaultdict(faker.email)
    # Iterate over the rows and yield anonymized rows.
    for row in rows:
        # Replace the name and email fields with faked fields.
        row['name']  = names[row['name']]
        row['email'] = emails[row['email']]
        # Yield the row back to the caller
        yield row
def anonymize(source, target):
    """
    The source argument is a path to a CSV file containing data to anonymize,
    while target is a path to write the anonymized CSV data to.
    """
    with open(source, 'rU') as f:
        with open(target, 'w') as o:
            # Use the DictReader to easily extract fields
            reader = csv.DictReader(f)
            writer = csv.DictWriter(o, reader.fieldnames)
            # Read and anonymize data, writing to target file.
            for row in anonymize_rows(reader):
                writer.writerow(row)
