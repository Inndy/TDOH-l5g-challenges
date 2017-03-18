orig = '''Google began in January 1996 as a research project by Larry Page and Sergey Brin when they were both PhD students at Stanford University in Stanford, California.[39]

While conventional search engines ranked results by counting how many times the search terms appeared on the page, the two theorized about a better system that analyzed the relationships between websites.[40] They called this new technology PageRank; it determined a website's relevance by the number of pages, and the importance of those pages, that linked back to the original site.[41][42]

Page and Brin originally nicknamed their new search engine "BackRub", because the system checked backlinks to estimate the importance of a site.[43][44][45] Eventually, they changed the name to Google, originating from a misspelling of the word "googol",[46][47] the number one followed by one hundred zeros, which was picked to signify that the search engine was intended to provide large quantities of information.[48] Originally, Google ran under Stanford University's website, with the domains google.stanford.edu and z.stanford.edu.[49][50]

The domain name for Google was registered on September 15, 1997,[51] and the company was incorporated on September 4, 1998. It was based in the garage of a friend (Susan Wojcicki[39]) in Menlo Park, California. Craig Silverstein, a fellow PhD student at Stanford, was hired as the first employee.[39][52][53]
'''

diff = '''GoogleT began in January 1996 as a research project by Larry Page and Sergey Brin when they were both PhDD students at Stanford University in Stanford, California.[39]

While conventional search engines ranked results by counting how many times the search terms appeared on the page, the two theorized about aO better system that analyzed the relationships between websites.H[40] They called this new technology PageRank; it determined a website's relevance by the number of pages, and the importance of those pages, that linked back to the original site.{[41][42]

Page and Brinj originally nicknamed their new search engine "BackRubu", because the system checked backlinks to estimates the importance of a site.[43][44][45] Evetntually, they changed the name to Google, originating from a misspelling of the word "googol",_[46][47] the number oneg folloowed by oone hundred zeros, which was picked to signify that the search engine was intended to provide large quantities of information.[48] Originally, Google ran under Stanford University's website, with the domains googleg.stanford.edu and z.stanford.edul.[49][50]

The domain namee for Google was registered on September 15, 1997,_[51] and the company was incorporated on September 4, 1998. It was based in the garagie of a friend (Susan Wojcicki[39]) in Menlot Park, California. Craig Silverstein, a fellow PhD student at Stanford, was hired as the first employee.[39][52][53]}'''

i = j = 0
flag = ''

while j < len(diff):
    if orig[i] == diff[j]:
        i += 1
        j += 1
    else:
        flag += diff[j]
        j += 1

print(flag)
