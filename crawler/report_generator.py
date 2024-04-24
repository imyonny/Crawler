import os


class ReportGenerator:
    REPORT_WIDTH = 50  # Constant representing the width of report separators

    def __init__(self):
        reports_dir = "report"
        self.report_file = os.path.join(reports_dir, "links.txt")
        self.broken_links_file = os.path.join(reports_dir, "broken_links.txt")
        self.duplicate_images_file = os.path.join(reports_dir, "duplicate_images.txt")
        self.report = []
        self.broken_links = []
        self.duplicate_images = set()

    def add_link(self, url, depth):
        self.report.append((url, depth))

    def add_broken_link(self, url, status):
        self.broken_links.append((url, status))

    def add_image_url(self, image_url):
        self.duplicate_images.add(image_url)

    def generate_report(self):
        self._create_reports_dir()
        self._generate_report_file()
        self._generate_broken_links_file()
        self._generate_duplicate_images_file()

    def _create_reports_dir(self):
        reports_dir = "report"
        if not os.path.exists(reports_dir):
            os.makedirs(reports_dir)

    def _generate_report_file(self):
        with open(self.report_file, mode='w') as file:
            file.write("LINKS\n")
            file.write("-" * self.REPORT_WIDTH + "\n\n")
            for url, depth in self.report:
                file.write(f"URL: {url}\n")
                file.write(f"Depth: {depth}\n\n")

    def _generate_broken_links_file(self):
        with open(self.broken_links_file, mode='w') as file:
            file.write("BROKEN LINKS\n")
            file.write("-" * self.REPORT_WIDTH + "\n\n")
            for url, status in self.broken_links:
                file.write(f"URL: {url}\n")
                file.write(f"Status: {status}\n\n")

    def _generate_duplicate_images_file(self):
        with open(self.duplicate_images_file, mode='w') as file:
            file.write("DUPLICATE IMAGE URLs\n")
            file.write("-" * self.REPORT_WIDTH + "\n\n")
            for image_url in self.duplicate_images:
                file.write(f"- {image_url}\n")
