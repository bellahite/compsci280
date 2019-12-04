class Delivery_personnel:
	def __init__(self, name, years_of_services, company, is_drone, zip_codes_covered):
		self.name 			   = name 
		self.years_of_services = years_of_services
		self.company 		   = company
		self.is_drone 		   = is_drone
		self.zip_codes_covered = zip_codes_covered

	def get_years(self):
		return(self.years_of_services)

	def get_company(self):
		return(self.company)

	def get_zipcodes(self):
		return(self.zip_codes_covered)

	def set_years(self, d):
		self.years_of_services = d 

	def set_company(self, d):
		self.company = d

	def set_zipcodes(self, d):
		self.zip_codes_covered = d 

	def deliver(self, d):
		if(self.zip_codes_covered == 1):
			return d
		else:
			return(d * deliver(d-1))
