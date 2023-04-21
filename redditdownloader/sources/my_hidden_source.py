from sources import source
import static.praw_wrapper as reddit


class Hidden(source.Source):
	def __init__(self):
		super().__init__(source_type='personal-hidden',
						 description="Submissions and Comments you've hidden.")

	def get_elements(self):
		for ele in reddit.my_hidden():
			if self.check_filters(ele):
				yield ele

	def get_settings(self):  # !cover
		return []

	def get_config_summary(self):  # !cover
		return "Scanning all your Hidden posts."
