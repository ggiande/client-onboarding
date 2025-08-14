import csv
from io import StringIO

class CSVMarshaller:
    """
   A class to handle the marshalling and unmarshalling of Person objects
   to and from a single CSV record.
   """
    # UNMARSHALLING / DESERIALIZING
    @staticmethod
    def unmarshal(self, csv_record: str) -> Person:
        """
        Converts a single CSV record string into a Person object.
        This is the process of unmarshalling.
        """
        # Use StringIO to treat the string as a file, which the csv module can read.
        f = StringIO(csv_record)
        reader = csv.reader(f)

        # Get the first (and only) row from the CSV.
        row = next(reader)

        # Create a new Person object from the data in the row.
        # The `*row` unpacks the list of strings into arguments for the Person constructor.
        return Person(*row)

    # SERIALIZING / MARSHALLING
    @staticmethod
    def marshal(self, person_obj: Person) -> str:
        """
        Converts a Person object back into a CSV record string.
        This is the process of marshalling.
        """
        # Use StringIO to capture the output of the csv writer.
        f = StringIO()
        writer = csv.writer(f)

        # Write the object's data as a single row.
        writer.writerow([person_obj.name, person_obj.age, person_obj.city])

        # Get the string value from the StringIO object and strip the trailing newline.
        return f.getvalue().strip()