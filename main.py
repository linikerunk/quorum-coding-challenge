import csv
import os


if not os.path.exists("result_data"):
        os.mkdir("result_data")


class ReadCSV:

    @staticmethod
    def read(file_name, callback) -> list:
        """This function reads a csv file and returns a list of lists"""
        with open(file_name, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                callback(row)
            return callback


class LegislatorsSupportOppose:
    state: dict = {}
    file = open("result_data/legislators-support-oppose-count.csv", "w", newline="")

    def execute(self, row) -> dict:
        """This function returns execute all flows of create_file_legislator_support_opposed"""
        if row[0] == 'id':
            writer = csv.writer(self.file)
            writer.writerow(['id', 'name', 'num_supported_bills', 'num_opposed_bills'])
            return

        self.state['id_legislator'], self.state['name'] = row[0], row[1]
        self.state['num_supported_bills'], self.state['num_opposed_bills'] = 0, 0
        self.check_vote_results_per_legislator()
        writer = csv.writer(self.file)
        writer.writerow(self.state.values())

    def create_file_legislator_support_opposed(self, row) -> dict:
        """This function returns a dict with the vote results"""
        self.treat_data_legislator_support_opposed(row)

    def treat_data_legislator_support_opposed(self, row)-> dict:
        """ This function should return a dict with title id, name, num_supported_bills and num_opposed_bills:
            vote_type 1 = supported
            vote_type 2 = opposed 
        """
        if row[0] == 'id':
            return

        if self.state['id_legislator'] == row[1]:
            if row[3] == '1':
                self.state['num_supported_bills'] += 1
            elif row[3] == '2':
                self.state['num_opposed_bills'] += 1

    def check_vote_results_per_legislator(self) -> dict:
        """"""
        ReadCSV().read(
            file_name='informations-csv/vote_results.csv',
            callback=self.create_file_legislator_support_opposed
        )


class Bills:
    state: dict = {}
    file = open("result_data/bills.csv", "w", newline="")

    def execute(self, row) -> dict:
        """This function returns execute all flows of create_file_bills"""
        if row[0] == 'id':
            writer = csv.writer(self.file)
            writer.writerow([
                'id',
                'name',
                'supporter_count',
                'opposer_count',
                'primary_sponsor'
            ])
            return

        self.state['id'], self.state['name'] = row[0], row[1]
        self.state['supporter_count'], self.state['opposer_count'] = 0, 0
        self.state['primary_sponsor_id'] = row[2]
        self.state['primary_sponsor'] = 'Unknown'
        self.create_file_bills()
        del self.state['vote_id']; del self.state['primary_sponsor_id']
        writer = csv.writer(self.file)
        writer.writerow(self.state.values())

    def get_legislator_by_sponsor_id(self) -> dict:
        """This function returns the information how many supporters \
        and opponents a bill and who helps the bill
        """
        ReadCSV().read(
            file_name='informations-csv/legislators.csv',
            callback=self.get_sponsor_by_bill,
        )

    def get_vote_id_by_bill_id(self) -> dict:
        """This function returns the vote results by bill"""
        ReadCSV().read(
            file_name='informations-csv/votes.csv',
            callback=self.get_votes_id,
        )

    def get_votes_id(self, row) -> dict:
        """This function returns the vote results by bill"""
        if row[0] == 'id':
            return
        if self.state['id'] == row[1]:
            self.state['vote_id'] = row[0]

    def get_sponsor_by_bill(self, row) -> dict:
        """This function returns the sponsor of the bill"""
        if row[0] == 'id':
            return

        if self.state['primary_sponsor_id'] == row[0]:
            self.state['primary_sponsor'] = row[1]
    
    def get_number_of_supporters_and_opposers(self) -> dict:
        ReadCSV().read(
            file_name='informations-csv/vote_results.csv',
            callback=self.get_number_of_supporters_and_opposers_by_vote_id,
        )
    
    def get_number_of_supporters_and_opposers_by_vote_id(self, row) -> dict:
        """This function returns the number of supporters and opponents by vote id"""
        if row[0] == 'id':
            return

        if self.state['vote_id'] == row[2]:
            if row[3] == '1':
                self.state['supporter_count'] += 1
            elif row[3] == '2':
                self.state['opposer_count'] += 1

    def create_file_bills(self) -> dict:
        """This function creates a file with the bills information"""""
        self.get_legislator_by_sponsor_id()
        self.get_vote_id_by_bill_id()
        self.get_number_of_supporters_and_opposers()


class Bootstrap:

    def run() -> None:
        """This function runs the application"""
        for question in questions:
            ReadCSV().read(
                file_name=question['filename'],
                callback=question['use_class']().execute
            )

question1 = {
    "filename": "informations-csv/legislators.csv",
    "use_class": LegislatorsSupportOppose
}
question2 = {
    "filename": "informations-csv/bills.csv",
    "use_class": Bills
}
questions = [question1, question2]

if __name__ == '__main__':
    Bootstrap.run()
