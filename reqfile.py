import requests
import bs4

main_url = "http://www.icd10data.com/"
url = "http://www.icd10data.com/ICD10CM/Codes"

     
def main_link_finder(url,link_class,text_class,link_start=0):
    """ Function to get all links from a page and subpage
    """
    page = requests.get(url)
    soup = bs4.BeautifulSoup(page.text,'html.parser')
    links = soup.find_all("a",class_=link_class,href=True)

    links_ = []
    for item in links:
        links_.append(item['href'])
    new_links = []
    for item in links_[link_start:]:
        new_links.append(main_url+item)    

    return new_links


def download_to_excel(url_lists):
    """ Function to save all links in a txt file
    """
    f = open('output.txt','w')
    for url_list in url_lists:
        for elt in url_list:
            f.write(elt+"\n")
    f.close()


if __name__ == "__main__":

    All_links = []

    #FOR FINDING ALL THE LINKS [Only the final sub-sub-links]
    # ex: http://www.icd10data.com/ICD10CM/Codes/Z00-Z99/Z19-Z19
    new_links = main_link_finder(url,'identifier',"body-content",21)
    print(len(new_links))

    # for fiding all the final links
    # ex: http://www.icd10data.com//ICD10CM/Codes/V00-Y99/V10-V19/V10-/V10.1
    for link in new_links:
        All_links.append(main_link_finder(link,'identifierSpacing identifier',"body-content"))
    download_to_excel(All_links)
