from logic import get_soup, date_setup, hash_

CORR_FORMAT_DATE = "%Y%m%d"
dict_url = {
    "voyager": "https://www.jpl.nasa.gov/missions/voyager-1/",
    "rfc": "https://datatracker.ietf.org/doc/rfc1149/history/",
    "brain_emoji": "https://www.unicode.org/Public/16.0.0/ucd/UnicodeData.txt",
    "genesis_block": "https://en.bitcoin.it/wiki/Genesis_block",
    "book_for_prog": "https://books.google.ru/books/about/The_C_Programming_Language.html?id=FGkPBQAAQBAJ&redir_esc=y"
}


def search_launch_voyager():
    url = dict_url["voyager"]
    soup = get_soup(url)
    data = soup.find("div", class_="lg:col-span-2 col-span-5").find_all("p")[1]
    date_text = data.text.replace("Sept.", "Sep", 1)
    date = date_setup(date_text, "%b %d, %Y", CORR_FORMAT_DATE)
    return date


def search_data_rfc():
    url = dict_url["rfc"]
    soup = get_soup(url)
    date_text = soup.find_all("tr")[4].find("td").find("div").text
    date = date_setup(date_text, "%Y-%m-%d", CORR_FORMAT_DATE)
    return date


def search_brain_codepoint():
    url = dict_url["brain_emoji"]
    soup = get_soup(url)
    codepoint = str([value.split(";")[0] for value in soup.text.split() if "BRAIN" in value][0])
    return codepoint


def date_genesis_bitcoin_block():
    url = dict_url["genesis_block"]
    soup = get_soup(url)
    date_text = soup.find("blockquote").text.split()[2]
    date = date_setup(date_text, "%d/%b/%Y", CORR_FORMAT_DATE)
    return date


def search_book_isbn():
    url = dict_url["book_for_prog"]
    soup = get_soup(url)
    block_text = [el.text for el in soup.find("table", id="metadata_content_table").find_all("tr") if 'ISBN' in el.text]
    isbn = block_text[0].split(", ")[0]
    return isbn.replace("ISBN", "", 1)


def run_parser():
    flag = "FLAG{19770905-19900401-1F9E0-20090103-0131103628}"
    result_hash = hash_(flag)
    correct_answer = "d311f26ea1a995af669a62758ad5e0ce2583331059fbfc5c04cc84b2d41f4aed"
    print(result_hash)
    print("Status:", correct_answer == result_hash)

    # можно при желании вывести переменные, чтобы сравнить значения с флагом:
    # voyager_date = search_launch_voyager()
    # rfc1149_date = search_data_rfc()
    # brain_codepoint = search_brain_codepoint()
    # btc_genesis_date = date_genesis_bitcoin_block()
    # kr2_isbn10 = search_book_isbn()
    # print(voyager_date)
    # print(rfc1149_date)
    # print(brain_codepoint)
    # print(btc_genesis_date)
    # print(kr2_isbn10)


run_parser()