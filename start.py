from icrawler.builtin import GoogleImageCrawler

def google_image_downloader(query):
    crawler = GoogleImageCrawler(storage={'root_dir': './img'})
    crawler.crawl(keyword=f'{query}', max_num=1, overwrite=True)